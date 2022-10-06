#include <pybind11/pybind11.h>
namespace py = pybind11;


struct Pet {
    Pet(const std::string &name) : name(name) { }
    std::string name;
};

struct Dog : Pet {
    Dog(const std::string &name) : Pet(name) { }
    std::string bark() const { return "woof!"; }
};


PYBIND11_MODULE(example, m) {
    py::class_<Pet> pet(m, "Pet");
    pet.def(py::init<const std::string &>())
       .def_readwrite("name", &Pet::name);
    
    // Method 2: pass parent class_ object:
    py::class_<Dog>(m, "Dog", pet /* <- specify Python parent type */)
        .def(py::init<const std::string &>())
        .def("bark", &Dog::bark);
    m.def("pet_store", []() { return std::unique_ptr<Pet>(new Dog("Molly")); });
}

