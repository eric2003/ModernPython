cmake_minimum_required ( VERSION 3.20 )

project ( testprj )

set ( PRJ_INCLUDE_DIRS )
set ( PRJ_COMPILE_FEATURES )
set ( PRJ_LIBRARIES )

list ( APPEND PRJ_COMPILE_FEATURES cxx_std_20 )

find_package(pybind11 CONFIG REQUIRED)

#  set_property(
#    TARGET pybind11::pybind11
#    APPEND
#    PROPERTY INTERFACE_COMPILE_DEFINITIONS Py_DEBUG)

message ( STATUS "PYTHON_IS_DEBUG = ${PYTHON_IS_DEBUG} " )
message ( STATUS "pybind11_FOUND = ${pybind11_FOUND} " )
message ( STATUS "pybind11_VERSION = ${pybind11_VERSION} " )
message ( STATUS "pybind11_VERSION_TYPE = ${pybind11_VERSION_TYPE} " )
message ( STATUS "pybind11_INCLUDE_DIRS = ${pybind11_INCLUDE_DIRS} " )
message ( STATUS "pybind11_INCLUDE_DIR = ${pybind11_INCLUDE_DIR} " )
message ( STATUS "pybind11_DEFINITIONS = ${pybind11_DEFINITIONS} " )
message ( STATUS "pybind11_LIBRARIES = ${pybind11_LIBRARIES} " )
message ( STATUS "pybind11_LIBRARY = ${pybind11_LIBRARY} " )

include(CMakePrintHelpers)
cmake_print_properties(
  TARGETS pybind11::module
  PROPERTIES LINK_LIBRARIES
)

cmake_print_properties(
  TARGETS pybind11::module
  PROPERTIES INTERFACE_LINK_LIBRARIES
)

cmake_print_properties(
  TARGETS pybind11::module
  PROPERTIES COMPILE_FEATURES
)


list ( APPEND PRJ_LIBRARIES pybind11::module )

# Create an extension module
add_library(mylib MODULE main.cpp)

target_include_directories ( mylib
    PRIVATE 
        ${PRJ_INCLUDE_DIRS}
)

target_link_libraries( mylib
    PRIVATE 
        ${PRJ_LIBRARIES}
)

target_compile_features ( mylib
    PRIVATE 
        ${PRJ_COMPILE_FEATURES}
)
