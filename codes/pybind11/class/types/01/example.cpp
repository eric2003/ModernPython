#include <pybind11/pybind11.h>
namespace py = pybind11;

struct Pet {
    enum Kind {
        Dog = 0,
        Cat
    };

    struct Attributes {
        float age = 0;
    };

    Pet(const std::string &name, Kind type) : name(name), type(type) { }

    std::string name;
    Kind type;
    Attributes attr;
};


PYBIND11_MODULE(example, m) {
    py::class_<Pet> pet(m, "Pet");
    
    pet.def(py::init<const std::string &, Pet::Kind>())
        .def_readwrite("name", &Pet::name)
        .def_readwrite("type", &Pet::type)
        .def_readwrite("attr", &Pet::attr);
    
    py::enum_<Pet::Kind>(pet, "Kind")
        .value("Dog", Pet::Kind::Dog)
        .value("Cat", Pet::Kind::Cat)
        .export_values();
    
    py::class_<Pet::Attributes> attributes(pet, "Attributes");
    attributes.def(py::init<>())
              .def_readwrite("age", &Pet::Attributes::age);
}

