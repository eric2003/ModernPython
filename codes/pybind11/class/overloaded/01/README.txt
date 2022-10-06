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

p = example.pet_store2()
type(p)
PolymorphicDog  # automatically downcast
p.bark()
u'woof!'