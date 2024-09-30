# Minimum required version of CMake
cmake_minimum_required(VERSION 3.10)
add_compile_options("/utf-8")

# Project name and version
project(CSVHandlerProject VERSION 1.0)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Include directory for header files
include_directories(include)

# Add the source file in lib directory
# 自动收集所有在 lib 文件夹下的源文件
file(GLOB SOURCE_FILES "${CMAKE_SOURCE_DIR}/lib/*.cpp")

# Add executable target for the main.cpp in the root directory
add_executable(main main.cpp)
target_sources(main PRIVATE ${SOURCE_FILES})

# # Add the executable target for the test files in the test directory
# add_executable(test_csv test/test.cpp)
# add_executable(new_module test/new_module_by_template.cpp)

# # Link the CSVHandler library to the test executable
# target_sources(test_csv PRIVATE ${SOURCES})

# 启用 CMake 的测试功能
enable_testing()

# 查找 Google Test 库
find_package(GTest CONFIG REQUIRED)

# 包含头文件的目录（你之前的配置）
include_directories(include)

# 为你的测试源文件创建可执行目标（例如 test_csv）
add_executable(test_csv test/test.cpp)
target_sources(test_csv PRIVATE ${SOURCE_FILES})

# 将 GTest 链接到测试可执行目标中
target_link_libraries(test_csv PRIVATE GTest::gtest GTest::gtest_main)

# 添加一个测试，使用 test_csv 可执行文件
add_test(NAME AllTestsInMain COMMAND test_csv)
