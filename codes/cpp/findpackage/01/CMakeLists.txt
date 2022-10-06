cmake_minimum_required ( VERSION 3.20 )

project ( testprj )

set ( PRJ_INCLUDE_DIRS )
set ( PRJ_COMPILE_FEATURES )
set ( PRJ_LIBRARIES )

list ( APPEND PRJ_COMPILE_FEATURES cxx_std_20 )

find_package(PythonLibs)

message ( STATUS "PYTHON_IS_DEBUG = ${PYTHON_IS_DEBUG} " )
message ( STATUS "PythonLibs_FOUND = ${PythonLibs_FOUND} " )
message ( STATUS "PythonLibs_VERSION = ${PythonLibs_VERSION} " )
message ( STATUS "PythonLibs_VERSION_TYPE = ${PythonLibs_VERSION_TYPE} " )
message ( STATUS "PythonLibs_INCLUDE_DIRS = ${PythonLibs_INCLUDE_DIRS} " )
message ( STATUS "PythonLibs_INCLUDE_DIR = ${PythonLibs_INCLUDE_DIR} " )
message ( STATUS "PythonLibs_DEFINITIONS = ${PythonLibs_DEFINITIONS} " )
message ( STATUS "PythonLibs_LIBRARIES = ${PythonLibs_LIBRARIES} " )
message ( STATUS "PythonLibs_LIBRARY = ${PythonLibs_LIBRARY} " )

message ( STATUS "CMAKE_VERSION = ${CMAKE_VERSION} " )

include(CMakePrintHelpers)