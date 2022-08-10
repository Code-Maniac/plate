cmake_minimum_required(VERSION 3.14)
project(_PROJECTNAME_ VERSION 0.1 LANGUAGES C)

set(CMAKE_EXPORT_COMPILE_COMMANDS on)

# build with c++20 standard
set(CMAKE_CXX_STANDARD 11)

set(PROJECT_SOURCES
    src/main.c)

add_executable(_PROJECTNAME_ ${PROJECT_SOURCES})

add_custom_command(
    TARGET _PROJECTNAME_
    PRE_BUILD
    COMMAND ../scripts/pre-build.sh)

add_custom_command(
    TARGET _PROJECTNAME_
    POST_BUILD
    COMMAND ../scripts/post-build.sh)
