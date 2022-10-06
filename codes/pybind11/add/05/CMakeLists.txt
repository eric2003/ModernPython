cmake_minimum_required ( VERSION 3.20 )

project ( testprj )

set ( PRJ_INCLUDE_DIRS )
set ( PRJ_COMPILE_FEATURES )
set ( PRJ_LIBRARIES )

list ( APPEND PRJ_COMPILE_FEATURES cxx_std_20 )

find_package(pybind11 CONFIG REQUIRED)
#find_package(pybind11)

get_directory_property( my_system_targets DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} BUILDSYSTEM_TARGETS )
get_directory_property( my_import_targets DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} IMPORTED_TARGETS )

message( STATUS "my_system_targets=${my_system_targets}" )
message( STATUS "my_import_targets=${my_import_targets}" )

include ( ${CMAKE_CURRENT_SOURCE_DIR}/cmake/prop.cmake )

foreach (tgt ${my_import_targets})
    message ( STATUS " tgt = ${tgt} " )
    print_target_properties( ${tgt} )
endforeach()

message ( STATUS "PYTHON_IS_DEBUG = ${PYTHON_IS_DEBUG} " )
message ( STATUS "pybind11_FOUND = ${pybind11_FOUND} " )

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
