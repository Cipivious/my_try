cmake_minimum_required(VERSION 3.14)  # FetchContent is available in CMake 3.11+

project("my-project")

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add source to this project's executable.
add_executable(my-executable "main.cpp")

# Fetch nlohmann/json from its GitHub repository
include(FetchContent)
FetchContent_Declare(
  json
  GIT_REPOSITORY https://github.com/nlohmann/json.git
  GIT_TAG v3.10.5  # specify the version you need
)

# Make the fetched content available.
FetchContent_MakeAvailable(json)

# Link the json library
target_link_libraries(my-executable PRIVATE nlohmann_json)
