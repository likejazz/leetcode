cmake_minimum_required(VERSION 3.14)
project(leetcode)

set(CMAKE_CXX_STANDARD 17)

# Google Test
include(FetchContent)
FetchContent_Declare(
        googletest
        # Specify the commit you depend on and update it regularly.
        URL https://github.com/google/googletest/archive/609281088cfefc76f9d0ce82e1ff6c30cc3591e5.zip
)
FetchContent_MakeAvailable(googletest)

# Now simply link against gtest or gtest_main as needed. Eg
add_executable(testcase test_leetcode.cpp)
target_link_libraries(testcase gtest_main)
