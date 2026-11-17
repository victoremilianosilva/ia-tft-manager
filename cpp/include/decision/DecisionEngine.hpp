
#pragma once

namespace tft::decision {

class DecisionEngine {
public:
    DecisionEngine() = default;

    const char* version() const noexcept;
};

} // namespace tft::decision
