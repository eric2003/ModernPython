## https://stackoverflow.com/questions/32183975/how-to-print-all-the-properties-of-a-target-in-cmake/56738858#56738858
## https://stackoverflow.com/a/56738858/3743145

## Get all properties that cmake supports
execute_process(COMMAND cmake --help-property-list OUTPUT_VARIABLE CMAKE_PROPERTY_LIST)
## Convert command output into a CMake list
string(REGEX REPLACE ";" "\\\\;" CMAKE_PROPERTY_LIST "${CMAKE_PROPERTY_LIST}")
string(REGEX REPLACE "\n" ";" CMAKE_PROPERTY_LIST "${CMAKE_PROPERTY_LIST}")

list(REMOVE_DUPLICATES CMAKE_PROPERTY_LIST)
# Fix https://stackoverflow.com/questions/32197663/how-can-i-remove-the-the-location-property-may-not-be-read-from-target-error-i
list(FILTER CMAKE_PROPERTY_LIST EXCLUDE REGEX "^LOCATION$|^LOCATION_|_LOCATION$")
list(SORT CMAKE_PROPERTY_LIST)

function(print_target_properties tgt)
    if(NOT TARGET ${tgt})
      message("There is no target named '${tgt}'")
      return()
    endif()

    foreach (prop ${CMAKE_PROPERTY_LIST})
        #message ( STATUS " prop 1 = ${prop} " )
        string(TOUPPER ${CMAKE_BUILD_TYPE} BUILD_TYPE)
        string(REPLACE "<CONFIG>" "${BUILD_TYPE}" prop ${prop})
        #message ( STATUS " prop 2 = ${prop} " )
        get_target_property(propval ${tgt} ${prop})
        if (propval)
            #message ("${tgt} ${prop} = ${propval}")
            include(CMakePrintHelpers)
            cmake_print_properties(
               TARGETS ${tgt}
               PROPERTIES ${prop}
            )
        endif()
    endforeach()
endfunction()

