cmake_minimum_required ( VERSION 3.20 )

project ( testprj )

set ( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/modules/" )

set ( PRJ_INCLUDE_DIRS )
set ( PRJ_COMPILE_FEATURES )
set ( PRJ_LIBRARIES )

list ( APPEND PRJ_COMPILE_FEATURES cxx_std_20 )

find_package(Python3 COMPONENTS Interpreter Development)

find_package(NumPy)
if ( ${PYTHON_NUMPY_FOUND} )
  include_directories(${PYTHON_NUMPY_INCLUDE_DIR})
else()
  message(WARNING "Python3 NumPy not found, proceeding with -DWITHOUT_NUMPY."
  " Some functions might not work.")
  add_definitions(-DWITHOUT_NUMPY)
endif()

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