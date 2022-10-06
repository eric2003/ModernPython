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

p = Pet("Lucy", Pet.Cat)
p.type
Kind.Cat
int(p.type)
1L

p = example.Pet("Lucy", example.Pet.Cat)
>>> p = example.Pet("Lucy", Pet.Cat)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Pet' is not defined. Did you mean: 'set'?
>>> p = example.Pet("Lucy", example.Pet.Cat)
>>> p.type
<Kind.Cat: 1>
>>> int(p.type)
1
>>> Pet.Kind.__members__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Pet' is not defined. Did you mean: 'set'?
>>> example.Pet.Kind.__members__
{'Dog': <Kind.Dog: 0>, 'Cat': <Kind.Cat: 1>}
>>>

//p = Pet("Lucy", Pet.Cat)
p = example.Pet("Lucy", Pet.Cat)
pet_type = p.type
pet_type
Pet.Cat
str(pet_type)
'Pet.Cat'
pet_type.name
'Cat'