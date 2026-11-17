"""Streaming audit for fine-tuning traces and paired matches; emits compact Markdown."""
import argparse, json, math, statistics
from collections import Counter, defaultdict
from pathlib import Path

ACTIONS={0:"BUY",1:"REROLL",2:"BUY_XP",3:"MOVE_BENCH",4:"MOVE_BOARD",5:"SELL",6:"PASS",7:"EQUIP_FROM_INVENTORY",8:"CRAFT_AND_EQUIP"}
ECON=("BUY","BUY_XP","REROLL","PASS")

def records(path):
    with Path(path).open("r",encoding="utf-8-sig") as f:
        for n,line in enumerate(f,1):
            if line.strip():
                try: row=json.loads(line)
                except json.JSONDecodeError as e: raise ValueError(f"JSONL inválido {path}:{n}: {e}") from e
                if not isinstance(row,dict): raise ValueError(f"Registro inválido {path}:{n}")
                yield row

def load(path): return json.loads(Path(path).read_text(encoding="utf-8-sig"))
def action(row,key):
    try: return ACTIONS.get(int((row.get(key) or [])[0]),"UNKNOWN")
    except (ValueError,TypeError,IndexError): return "UNKNOWN"
def pct(n,d): return f"{100*n/d:.1f}%" if d else "n/a"
def avg(v):
    v=[float(x) for x in v if x is not None]
    return statistics.fmean(v) if v else None
def fmt(v): return "n/a" if v is None else f"{v:+.3f}"
def bucket(v,limits,labels):
    if v is None: return "desconhecido"
    for limit,label in zip(limits,labels):
        if float(v)<limit: return label
    return labels[-1]
def add(store,key,a,b,diff):
    x=store[key]; x["n"]+=1; x["diff"]+=int(diff); x["a"][a]+=1; x["b"][b]+=1

def trace_audit(path,selected):
    total=Counter(); aa=Counter(); bb=Counter()
    strategies=defaultdict(lambda:{"n":0,"diff":0,"a":Counter(),"b":Counter()})
    cohorts=defaultdict(lambda:{"n":0,"diff":0,"a":Counter(),"b":Counter()})
    scenarios=Counter(); target_n=target_diff=outside_n=outside_diff=0; missing=Counter()
    for row in records(path):
        a,b=action(row,"original_action"),action(row,"finetuned_action")
        diff=row.get("original_action")!=row.get("finetuned_action")
        aa[a]+=1; bb[b]+=1; total["n"]+=1; total["diff"]+=int(diff)
        s=row.get("state") or {}
        for field in ("hp","gold","level","stage","strategy_name"):
            if s.get(field) is None: missing[field]+=1
        strategy=str(s.get("strategy_name","UNKNOWN"))
        add(strategies,strategy,a,b,diff)
        gold,hp=s.get("gold"),s.get("hp")
        add(cohorts,"ouro "+bucket(gold,[50,60,80],["<50","50–59","60–79","80+"]),a,b,diff)
        add(cohorts,"HP "+bucket(hp,[20.000001,40.000001],["≤20","21–40",">40"]),a,b,diff)
        if gold is not None and float(gold)>=50:
            add(cohorts,"ouro ≥50",a,b,diff)
            if hp is not None and float(hp)<=30: add(cohorts,"ouro ≥50 + HP ≤30",a,b,diff)
            if strategy.upper()=="SLOWROLL": add(cohorts,"SLOWROLL + ouro ≥50",a,b,diff)
        if strategy.upper()=="FAST8" and gold is not None and float(gold)>=50:
            add(cohorts,"FAST8 + ouro ≥50",a,b,diff)
        ids=row.get("scenario_ids") or []; scenarios.update(ids)
        if selected in ids: target_n+=1; target_diff+=int(diff)
        else: outside_n+=1; outside_diff+=int(diff)
    return {"total":total,"aa":aa,"bb":bb,"strategies":strategies,"cohorts":cohorts,
            "scenarios":scenarios,"target_n":target_n,"target_diff":target_diff,
            "outside_n":outside_n,"outside_diff":outside_diff,"missing":missing}

def paired_audit(path):
    seeds=[]; aa=Counter(); bb=Counter(); deltas=defaultdict(list); completed=same=0
    for row in records(path):
        ok=bool(row.get("both_completed")); completed+=int(ok); same+=int(bool(row.get("same_initial_state")))
        for side,counter in (("original",aa),("finetuned",bb)):
            for counts in (row.get(side) or {}).get("action_counts",[]) or []: counter.update(counts or {})
        players=row.get("final_player_deltas") or []
        valid=[p for p in players if p.get("placement_delta") is not None]
        seed={"seed":row.get("seed"),"completed":ok,"same":bool(row.get("same_initial_state")),
              "reward":row.get("mean_reward_delta"),"placement":avg([p.get("placement_delta") for p in valid]),
              "top4":avg([int(bool(p["finetuned_top4"]))-int(bool(p["original_top4"])) for p in players
                          if p.get("finetuned_top4") is not None and p.get("original_top4") is not None])}
        seeds.append(seed)
        if ok:
            for p in players:
                for k in ("placement_delta","hp_delta","gold_delta","level_delta","board_power_delta",
                          "board_quality_score_delta","board_positional_score_delta","board_structural_score_delta"):
                    if p.get(k) is not None: deltas[k].append(float(p[k]))
    valid=[s for s in seeds if s["completed"]]
    placements=[s["placement"] for s in valid if s["placement"] is not None]
    ci=None
    if len(placements)>1:
        se=statistics.stdev(placements)/math.sqrt(len(placements))
        ci=(statistics.fmean(placements)-1.96*se,statistics.fmean(placements)+1.96*se)
    return {"seeds":seeds,"aa":aa,"bb":bb,"deltas":deltas,"completed":completed,"same":same,
            "placements":placements,"ci":ci,"valid":valid}

def action_table(aa,bb):
    lines=["| Ação | Original | Fine-tuned | Δ |","|---|---:|---:|---:|"]
    for name in ACTIONS.values(): lines.append(f"| {name} | {aa[name]} | {bb[name]} | {bb[name]-aa[name]:+d} |")
    return "\n".join(lines)

def cohort_table(data,keys):
    lines=["| Coorte | Estados | Divergência | BUY Δ | XP Δ | REROLL Δ | PASS Δ |","|---|---:|---:|---:|---:|---:|---:|"]
    for key in keys:
        x=data[key]; ds=[x["b"][n]-x["a"][n] for n in ECON]
        lines.append(f"| {key} | {x['n']} | {pct(x['diff'],x['n'])} | "+" | ".join(f"{v:+d}" for v in ds)+" |")
    return "\n".join(lines)

def render_trace(x,scenario):
    ckeys=[k for k in ("ouro ≥50","ouro ≥50 + HP ≤30","FAST8 + ouro ≥50","SLOWROLL + ouro ≥50",
                       "ouro <50","ouro 50–59","ouro 60–79","ouro 80+","HP ≤20","HP 21–40","HP >40") if k in x["cohorts"]]
    strategies=cohort_table(x["strategies"],sorted(x["strategies"]))
    coverage="\n".join(f"| {k} | {v} |" for k,v in sorted(x["scenarios"].items()))
    t=x["total"]
    return f"""## Análise shadow por estado

- Estados comparados: **{t['n']}**
- Ações divergentes: **{t['diff']} ({pct(t['diff'],t['n'])})**
- Estados do cenário {scenario}: **{x['target_n']}**, divergência **{pct(x['target_diff'],x['target_n'])}**
- Estados fora do cenário: **{x['outside_n']}**, divergência **{pct(x['outside_diff'],x['outside_n'])}**

### Frequência de ações
{action_table(x['aa'],x['bb'])}

### Economia por coorte
{cohort_table(x['cohorts'],ckeys)}

### Decisões por estratégia
{strategies}

### Cobertura observada dos cenários
| Cenário | Estados |
|---|---:|
{coverage}

As contagens não provam qualidade por si só. O trace registra HP, ouro, nível, estágio, round e estratégia, mas não qualidade da loja, campeões disponíveis, pares ou upgrades.
"""

def render_paired(x):
    seeds=["| Seed | Reward Δ | Placement Δ | Top4 Δ | Concluída | Estado inicial igual |","|---:|---:|---:|---:|:---:|:---:|"]
    for s in x["seeds"]:
        seeds.append(f"| {s['seed']} | {fmt(s['reward'])} | {fmt(s['placement'])} | {fmt(s['top4'])} | {'Sim' if s['completed'] else 'Não'} | {'Sim' if s['same'] else 'Não'} |")
    metrics=["| Métrica | Delta médio por jogador pareado |","|---|---:|"]
    for key,label in (("placement_delta","Colocação (negativo é melhor)"),("hp_delta","HP"),("gold_delta","Ouro final"),
                      ("level_delta","Nível"),("board_power_delta","Poder do tabuleiro"),
                      ("board_quality_score_delta","Qualidade do tabuleiro"),("board_positional_score_delta","Posicionamento"),
                      ("board_structural_score_delta","Estrutura")):
        metrics.append(f"| {label} | {fmt(avg(x['deltas'].get(key,[])))} |")
    ci=x["ci"]; ci_text=f"[{fmt(ci[0])}, {fmt(ci[1])}]" if ci else "n/a"
    p=x["placements"]; wins=sum(v<0 for v in p); losses=sum(v>0 for v in p); ties=sum(v==0 for v in p)
    return f"""## Partidas completas pareadas

- Seeds: **{len(x['seeds'])}**
- Pares concluídos: **{x['completed']}/{len(x['seeds'])}**
- Estados iniciais idênticos: **{x['same']}/{len(x['seeds'])}**
- Seeds com colocação melhor / pior / igual: **{wins} / {losses} / {ties}**
- Delta médio de colocação por seed: **{fmt(avg(p))}**
- IC 95% aproximado por seed: **{ci_text}**
- Delta médio de Top4 por seed: **{fmt(avg([s['top4'] for s in x['valid']]))}**

{chr(10).join(seeds)}

### Métricas terminais
{chr(10).join(metrics)}

### Ações nas partidas completas
{action_table(x['aa'],x['bb'])}

O intervalo usa seed como unidade amostral, não cada jogador individual, para evitar pseudorreplicação dentro da mesma lobby. É uma aproximação normal.
"""

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for arg in ("trace","paired","metadata","summary","output"): p.add_argument("--"+arg,required=True)
    a=p.parse_args()
    for path in (a.trace,a.paired,a.metadata,a.summary):
        if not Path(path).is_file(): raise FileNotFoundError(path)
    meta,summary=load(a.metadata),load(a.summary)
    scenario=meta.get("selected_scenario") or summary.get("selected_scenario")
    if meta.get("selected_scenario") and summary.get("selected_scenario") and meta["selected_scenario"]!=summary["selected_scenario"]:
        raise ValueError("Cenário divergente entre metadata e training summary.")
    tr=trace_audit(a.trace,scenario); pair=paired_audit(a.paired); missing=tr["missing"]
    missing_text=", ".join(f"{k}: {v}" for k,v in sorted(missing.items())) or "nenhum"
    report=f"""# Auditoria complementar de fine-tuning — {scenario or 'cenário não identificado'}

> Gerado por economy_finetuning/deep_audit.py. Os JSONL são processados em streaming; os dados brutos não são copiados para este Markdown.

## Resumo executivo

- Cenário: **{scenario or 'n/a'}**
- Transições do cenário no treino: **{summary.get('selected_scenario_transitions','n/a')}**
- Checkpoint original SHA-256: {summary.get('source_checkpoint_sha256',meta.get('checkpoint_sha256','n/a'))}
- Checkpoint fine-tuned SHA-256: {summary.get('finetuned_checkpoint_sha256',meta.get('finetuned_checkpoint_sha256','n/a'))}
- Campos ausentes no trace: **{missing_text}**

{render_trace(tr,scenario)}

{render_paired(pair)}

## Limitações e parecer

1. O trace não registra unidades da loja, pares, upgrades, composição planejada ou qualidade da oportunidade. Não é possível afirmar se uma compra específica era melhor que XP.
2. Não registra a identidade estratégica da unidade vendida. A preservação de pares/core não pode ser provada com estes arquivos.
3. Zero estados em uma coorte significa **não coberto**, não aprovado.
4. As métricas de lobby medem o resultado completo; não isolam causalmente uma ação individual.
5. O intervalo de confiança é aproximado e exige mais seeds inéditas para conclusões robustas.

- Estados SLOWROLL com ouro ≥50: **{tr['cohorts'].get('SLOWROLL + ouro ≥50',{}).get('n',0)}**
- Estados FAST8 com ouro ≥50: **{tr['cohorts'].get('FAST8 + ouro ≥50',{}).get('n',0)}**
- Estados com ouro ≥50 e HP ≤30: **{tr['cohorts'].get('ouro ≥50 + HP ≤30',{}).get('n',0)}**
- Amostra mínima de 20 seeds concluídas: **{'ATINGIDA' if len(pair['seeds'])>=20 and pair['completed']==len(pair['seeds']) else 'NÃO ATINGIDA'}**

**Este relatório não altera evaluation_review.json, não aprova o checkpoint e não libera o próximo cenário.**
"""
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(report,encoding="utf-8")
    print(f"Auditoria complementar gerada: {out}")
    print(f"Trace: {tr['total']['n']} estados; pareadas: {pair['completed']}/{len(pair['seeds'])} concluídas.")

if __name__=="__main__": main()
