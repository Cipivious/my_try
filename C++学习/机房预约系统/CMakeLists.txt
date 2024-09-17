# Minimum required version of CMake
cmake_minimum_required(VERSION 3.10)

# Project name and version
project(CSVHandlerProject VERSION 1.0)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Include directory for header files
include_directories(include)

# Add the source file in lib directory
set(SOURCES
    lib/CSVHandler.cpp
)

# Add executable target for the main.cpp in the root directory
add_executable(main main.cpp)
target_sources(main PRIVATE ${SOURCES})

# Add the executable target for the test files in the test directory
add_executable(test_csv test/test.cpp)
add_executable(new_module test/new_module_by_template.cpp)

# Link the CSVHandler library to the test executable
target_sources(test_csv PRIVATE ${SOURCES})
