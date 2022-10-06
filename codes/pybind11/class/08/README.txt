cmake -DBoost_DEBUG=ON ..
cmake -DCMAKE_TOOLCHAIN_FILE="C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake" ..
cmake -DCMAKE_TOOLCHAIN_FILE="C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake" \..
cmake .. -DCMAKE_TOOLCHAIN_FILE="C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake"
cmake .. -D CMAKE_TOOLCHAIN_FILE="C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake"
cmake -DCMAKE_BUILD_TYPE=Debug ..
cmake .. -D CMAKE_BUILD_TYPE=Debug -D CMAKE_TOOLCHAIN_FILE="C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake"
cmake .. -D CMAKE_BUILD_TYPE=Release -D CMAKE_TOOLCHAIN_FILE="C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake"

cmake .. -D PYTHON_IS_DEBUG=ON -D CMAKE_BUILD_TYPE=Debug -D CMAKE_TOOLCHAIN_FILE="C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake"
cmake .. -D CMAKE_BUILD_TYPE=Debug -D CMAKE_TOOLCHAIN_FILE="C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake"
cmake --build . --config Debug
cmake .. -D PYBIND11_DEBUG_MARKER=ON -D CMAKE_BUILD_TYPE=Debug -D CMAKE_TOOLCHAIN_FILE="C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake"
cmake .. -D CMAKE_BUILD_TYPE=Release -D CMAKE_TOOLCHAIN_FILE="C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake"

# Classic CMake
cd pybind11
mkdir build
cd build
cmake ..
make install

# CMake 3.15+
cd pybind11
cmake -S . -B build
cmake --build build -j 2  # Build on 2 cores
cmake --install build

cmake -S. -B build -D CMAKE_BUILD_TYPE=Release -D CMAKE_TOOLCHAIN_FILE="C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake"
cmake --build build --config Release -j 4
cmake --install build

By default, classes exported from C++ do not support this and the only writable attributes are the ones explicitly defined using class_::def_readwrite() or class_::def_property().

py::class_<Pet>(m, "Pet")
    .def(py::init<>())
    .def_readwrite("name", &Pet::name);
Trying to set any other attribute results in an error:

p = example.Pet()
p.name = "Charly"  # OK, attribute defined in C++
p.age = 2  # fail
AttributeError: 'Pet' object has no attribute 'age'