cmake -DBoost_DEBUG=ON ..
cmake -DCMAKE_TOOLCHAIN_FILE="C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake" ..

Properties for TARGET pybind11::module:
   pybind11::module.INTERFACE_LINK_LIBRARIES = 
   "pybind11::pybind11;
   pybind11::python_link_helper;
   $<$<OR:$<PLATFORM_ID:Windows>,$<PLATFORM_ID:Cygwin>>:
   $<BUILD_INTERFACE:
   optimized;
   C:/dev/vcpkg/installed/x64-windows/lib/python310.lib;
   debug;
   C:/dev/vcpkg/installed/x64-windows/debug/lib/python310_d.lib>>"