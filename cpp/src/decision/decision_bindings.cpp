
#include <pybind11/pybind11.h>

#include "decision/DecisionEngine.hpp"

namespace py = pybind11;

PYBIND11_MODULE(decision_engine, module) {
    module.doc() = "TFT Decision Engine";

    py::class_<tft::decision::DecisionEngine>(
        module,
        "DecisionEngine"
    )
        .def(py::init<>())
        .def("version", &tft::decision::DecisionEngine::version);
}
