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
