cmake_minimum_required ( VERSION 3.20 )

project ( testprj )

set ( PRJ_INCLUDE_DIRS )
set ( PRJ_COMPILE_FEATURES )
set ( PRJ_LIBRARIES )

list ( APPEND PRJ_COMPILE_FEATURES cxx_std_20 )

find_package(PythonLibs)

message ( STATUS "Python_FOUND = ${Python_FOUND} " )
message ( STATUS "PythonLibs_FOUND = ${PythonLibs_FOUND} " )
message ( STATUS "PYTHON_LIBRARIES = ${PYTHON_LIBRARIES} " )
message ( STATUS "PYTHON_INCLUDE_PATH = ${PYTHON_INCLUDE_PATH} " )
message ( STATUS "PYTHON_INCLUDE_DIRS = ${PYTHON_INCLUDE_DIRS} " )
message ( STATUS "PYTHON_DEBUG_LIBRARIES = ${PYTHON_DEBUG_LIBRARIES} " )
message ( STATUS "PYTHONLIBS_VERSION_STRING = ${PYTHONLIBS_VERSION_STRING} " )

message ( STATUS "CMAKE_VERSION = ${CMAKE_VERSION} " )

add_library( MyLib STATIC IMPORTED )

if ( TARGET Python::Interpreter )
    message ( STATUS "TARGET Python::Interpreter" )
endif()

include(CMakePrintHelpers)
cmake_print_properties(
  TARGETS MyLib
  PROPERTIES IMPORTED_LOCATION_DEBUG
)

cmake_print_properties(
  TARGETS MyLib
  PROPERTIES INTERFACE_LINK_LIBRARIES
)