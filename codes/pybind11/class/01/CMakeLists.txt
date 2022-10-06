cmake_minimum_required ( VERSION 3.20 )

project ( testprj )

find_package(Python COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(example example.cpp)

