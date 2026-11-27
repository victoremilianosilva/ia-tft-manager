#include <cassert>
#include <string>

#include <nlohmann/json.hpp>

#include "lobby/SemanticSha256.hpp"

int main() {
    using tft::semantic::sha256_hex;
    assert(sha256_hex("") ==
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855");
    assert(sha256_hex("abc") ==
        "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad");
    assert(sha256_hex("The quick brown fox jumps over the lazy dog") ==
        "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592");

    // Shared Python/C++ canonical JSON fixture: Unicode remains UTF-8,
    // empty arrays and null optionals retain their distinct representations,
    // and integer/float boundaries preserve Python json.dumps formatting.
    const nlohmann::json parity_payload = {
        {"empty", nlohmann::json::array()},
        {"limit", {-2147483648LL, 2147483647LL, 0.0, 1.0}},
        {"optional", nullptr},
        {"unicode", "Akame-赤い🌸"}
    };
    const auto canonical = parity_payload.dump(-1, ' ', false);
    assert(canonical == R"json({"empty":[],"limit":[-2147483648,2147483647,0.0,1.0],"optional":null,"unicode":"Akame-赤い🌸"})json");
    assert(sha256_hex(canonical) ==
        "2e2d30a202100fa3180341c79085abcaf66b0bd265bc933337d3e77a6819532e");
    return 0;
}
