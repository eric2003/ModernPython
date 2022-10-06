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
cmake .. -D PYBIND11_DEBUG_MARKER=ON -D CMAKE_BUILD_TYPE=Debug -D CMAKE_TOOLCHAIN_FILE="C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake"
