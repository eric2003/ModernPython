cmake_minimum_required ( VERSION 3.20 )

project ( testprj )

set ( PRJ_INCLUDE_DIRS )
set ( PRJ_COMPILE_FEATURES )
set ( PRJ_LIBRARIES )

list ( APPEND PRJ_COMPILE_FEATURES cxx_std_20 )

find_package(Python3 COMPONENTS Interpreter Development)


message ( STATUS "Python3_FOUND = ${Python3_FOUND} " )
message ( STATUS "Python3_INCLUDE_DIRS = ${Python3_INCLUDE_DIRS} " )
message ( STATUS "Python3_LIBRARIES = ${Python3_LIBRARIES} " )
message ( STATUS "Python3_ROOT_DIR = ${Python3_ROOT_DIR} " )
message ( STATUS "_PYTHON_PREFIX = ${_PYTHON_PREFIX} " )
message ( STATUS "Python3 = ${Python3} " )
message ( STATUS "Python3_CMAKE_ROLE = ${Python3_CMAKE_ROLE} " )

message ( STATUS "_PYTHON_PREFIX_REQUIRED_VERSION_MAJOR = _${_PYTHON_PREFIX}_REQUIRED_VERSION_MAJOR " )
message ( STATUS "Python3_LIBRARY_RELEASE = ${Python3_LIBRARY_RELEASE}" )
message ( STATUS "Python3_LIBRARY_DEBUG = ${Python3_LIBRARY_DEBUG}" )
message ( STATUS "Python3_RUNTIME_LIBRARY_RELEASE = ${Python3_RUNTIME_LIBRARY_RELEASE}" )
message ( STATUS "Python3_RUNTIME_LIBRARY_DEBUG = ${Python3_RUNTIME_LIBRARY_DEBUG}" )
message ( STATUS "Python3_INCLUDE_DIR = ${Python3_INCLUDE_DIR}" )
message ( STATUS "Python3_CONFIG = ${Python3_CONFIG}" )
message ( STATUS "Python3_DEVELOPMENT_MODULE_SIGNATURE = ${Python3_DEVELOPMENT_MODULE_SIGNATURE}" )
message ( STATUS "Python3_LIBRARY_TYPE = ${Python3_LIBRARY_TYPE}" )
message ( STATUS "IMPORTED_LOCATION = ${IMPORTED_LOCATION}" )
message ( STATUS "Python3_LINK_OPTIONS = ${Python3_LINK_OPTIONS}" )
message ( STATUS "CMAKE_LIBRARY_ARCHITECTURE = ${CMAKE_LIBRARY_ARCHITECTURE}" )
message ( STATUS "Python3_LIBRARY = ${Python3_LIBRARY}" )
message ( STATUS "Python3_LIB_NAMES = ${Python3_LIB_NAMES}" )
message ( STATUS "Python3_LIB_NAMES_DEBUG = ${Python3_LIB_NAMES_DEBUG}" )
message ( STATUS "Python3_COMPILER = ${Python3_COMPILER}" )
message ( STATUS "Python3_EXECUTABLE = ${Python3_EXECUTABLE}" )
message ( STATUS "Python3_LIBRARY = ${Python3_LIBRARY}" )
message ( STATUS "Python3_LIBRARIES = ${Python3_LIBRARIES}" )
message ( STATUS "Python3_LIBRARY_DIRS = ${Python3_LIBRARY_DIRS}" )
message ( STATUS "Python3_RUNTIME_LIBRARY_DIRS = ${Python3_RUNTIME_LIBRARY_DIRS}" )
message ( STATUS "Python3_USE_STATIC_LIBS = ${Python3_USE_STATIC_LIBS}" )
message ( STATUS "Python3_VERSION = ${Python3_VERSION}" )
message ( STATUS "Python3_LINK_OPTIONS = ${Python3_LINK_OPTIONS}" )
message ( STATUS "Python3_Interpreter_FOUND = ${Python3_Interpreter_FOUND}" )
message ( STATUS "Python3_EXECUTABLE = ${Python3_EXECUTABLE}" )
message ( STATUS "Python3_INTERPRETER_ID = ${Python3_INTERPRETER_ID}" )
message ( STATUS "Python3_STDLIB = ${Python3_STDLIB}" )
message ( STATUS "Python3_STDARCH = ${Python3_STDARCH}" )
message ( STATUS "Python3_SITELIB = ${Python3_SITELIB}" )
message ( STATUS "Python3_SITEARCH = ${Python3_SITEARCH}" )



if ( ${Python3_FOUND} )
    #include_directories(${Python3_INCLUDE_DIRS})
else()
    message ( FATAL_ERROR "Python3 not found, please install it." )
endif()

list ( APPEND PRJ_INCLUDE_DIRS ${Python3_INCLUDE_DIRS} )
list ( APPEND PRJ_LIBRARIES ${Python3_LIBRARIES} )

message ( STATUS "PRJ_LIBRARIES = ${PRJ_LIBRARIES} " )

add_executable ( ${PROJECT_NAME}
    main.cpp
)

target_include_directories ( ${PROJECT_NAME}
    PRIVATE 
        ${PRJ_INCLUDE_DIRS}
)

target_link_libraries( ${PROJECT_NAME} 
    PRIVATE 
        ${PRJ_LIBRARIES}
)

target_compile_features ( ${PROJECT_NAME} 
    PRIVATE 
        ${PRJ_COMPILE_FEATURES}
)