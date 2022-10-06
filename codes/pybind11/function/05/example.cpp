#include <pybind11/pybind11.h>
namespace py = pybind11;

int add(int i = 1, int j = 2)
{
    return i + j;
}

PYBIND11_MODULE(example, m)
{
    m.doc() = "pybind11 example plugin";

    // regular notation
    m.def("add1", &add, py::arg("i") = 1, py::arg("j") = 2);
    using namespace pybind11::literals;
    // shorthand
    m.def("add2", &add, "i"_a=1, "j"_a=2);
    // shorthand
    m.def("add3", &add, "m"_a=1, "n"_a=2);
}
