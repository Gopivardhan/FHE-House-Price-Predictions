cmake_minimum_required(VERSION 3.10)
project(house_price_prediction)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find OpenFHE package
find_package(OpenFHE REQUIRED)

# Include directories
include_directories(${OPENFHE_INCLUDE_DIRS})
include_directories(${OPENFHE_INCLUDE_DIRS}/core)
include_directories(${OPENFHE_INCLUDE_DIRS}/pke)

# Add executable
add_executable(app main.cpp yourSolution.cpp)

# Link against OpenFHE libraries
target_link_libraries(app ${OPENFHE_LIBRARIES})