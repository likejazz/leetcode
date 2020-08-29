cmake_minimum_required(VERSION 2.8)
project(leetcode)

set(CMAKE_CXX_STANDARD 17)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/googletest/include)
link_directories(${CMAKE_CURRENT_SOURCE_DIR}/googletest/lib)

add_executable(testcase test_leetcode.cpp ${SOURCE_FILES})
target_link_libraries(testcase gtest gtest_main)
