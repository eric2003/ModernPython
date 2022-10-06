cmake_minimum_required ( VERSION 3.20 )

project ( testprj )

set ( PRJ_INCLUDE_DIRS )
set ( PRJ_COMPILE_FEATURES )
set ( PRJ_LIBRARIES )

list ( APPEND PRJ_COMPILE_FEATURES cxx_std_20 )

find_package (Python COMPONENTS Interpreter Development)

get_cmake_property( varlist VARIABLES )
list ( SORT varlist )
foreach (_variableName ${varlist})
    message( STATUS "${_variableName}=${${_variableName}}" )
endforeach()

message ( STATUS "AVAILABLE_CONFIGURATION_TYPES = ${AVAILABLE_CONFIGURATION_TYPES} " )

message ( STATUS "CMAKE_PROPERTY_LIST = ${CMAKE_PROPERTY_LIST} " )
message ( STATUS "Python_FOUND = ${Python_FOUND} " )
message ( STATUS "PythonLibs_FOUND = ${PythonLibs_FOUND} " )
message ( STATUS "PYTHONLIBS_FOUND = ${PYTHONLIBS_FOUND} " )
message ( STATUS "Python_Interpreter_FOUND = ${Python_Interpreter_FOUND} " )
message ( STATUS "Python_EXECUTABLE = ${Python_EXECUTABLE} " )
message ( STATUS "Python_INTERPRETER_ID = ${Python_INTERPRETER_ID} " )
message ( STATUS "Python_STDLIB = ${Python_STDLIB} " )
message ( STATUS "Python_STDARCH = ${Python_STDARCH} " )
message ( STATUS "Python_SITELIB = ${Python_SITELIB} " )
message ( STATUS "Python_SITEARCH = ${Python_SITEARCH} " )
message ( STATUS "Python_SOABI = ${Python_SOABI} " )
message ( STATUS "Python_Compiler_FOUND = ${Python_Compiler_FOUND} " )
message ( STATUS "Python_COMPILER = ${Python_COMPILER} " )
message ( STATUS "Python_DOTNET_LAUNCHER = ${Python_DOTNET_LAUNCHER} " )
message ( STATUS "Python_Development_FOUND = ${Python_Development_FOUND} " )
message ( STATUS "Python_Development.Module_FOUND = ${Python_Development.Module_FOUND} " )
message ( STATUS "Python_Development.Embed_FOUND = ${Python_Development.Embed_FOUND} " )
message ( STATUS "Python_LINK_OPTIONS = ${Python_LINK_OPTIONS} " )
message ( STATUS "Python_INCLUDE_DIRS = ${Python_INCLUDE_DIRS} " )
message ( STATUS "PYTHON_INCLUDE_DIRS = ${PYTHON_INCLUDE_DIRS} " )
message ( STATUS "Python_LIBRARIES = ${Python_LIBRARIES} " )
message ( STATUS "Python_LIBRARY_DIRS = ${Python_LIBRARY_DIRS} " )
message ( STATUS "Python_RUNTIME_LIBRARY_DIRS = ${Python_RUNTIME_LIBRARY_DIRS} " )
message ( STATUS "Python_VERSION = ${Python_VERSION} " )
message ( STATUS "Python_VERSION_MAJOR = ${Python_VERSION_MAJOR} " )
message ( STATUS "Python_VERSION_MINOR = ${Python_VERSION_MINOR} " )
message ( STATUS "Python_VERSION_PATCH = ${Python_VERSION_PATCH} " )
message ( STATUS "Python_PyPy_VERSION = ${Python_PyPy_VERSION} " )
message ( STATUS "Python_NumPy_FOUND = ${Python_NumPy_FOUND} " )
message ( STATUS "Python_NumPy_INCLUDE_DIRS = ${Python_NumPy_INCLUDE_DIRS} " )
message ( STATUS "Python_NumPy_VERSION = ${Python_NumPy_VERSION} " )



message ( STATUS "PYTHON_LIBRARIES = ${PYTHON_LIBRARIES} " )
message ( STATUS "PYTHON_INCLUDE_PATH = ${PYTHON_INCLUDE_PATH} " )

message ( STATUS "PYTHON_DEBUG_LIBRARIES = ${PYTHON_DEBUG_LIBRARIES} " )
message ( STATUS "PYTHONLIBS_VERSION_STRING = ${PYTHONLIBS_VERSION_STRING} " )

message ( STATUS "CMAKE_VERSION = ${CMAKE_VERSION} " )

if ( TARGET Python::Interpreter )
    message ( STATUS "TARGET Python::Interpreter" )
endif()

include(CMakePrintHelpers)
cmake_print_properties(
  TARGETS Python::Python
  PROPERTIES IMPORTED_LOCATION_DEBUG
)

cmake_print_properties(
  TARGETS Python::Python
  PROPERTIES INTERFACE_LINK_LIBRARIES
)

cmake_print_properties(
  TARGETS Python::Python
  PROPERTIES COMPILE_DEFINITIONS
)

cmake_print_properties(
  TARGETS Python::Python
  PROPERTIES INCLUDE_DIRECTORIES
)

cmake_print_properties(
  TARGETS Python::Python
  PROPERTIES LINK_DIRECTORIES
)

