cmake_minimum_required(VERSION 3.31.0)

set(CXX_STANDARD 23)
set(CXX_STANDARD_REQUIRED ON)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

## Install Conan Dependencies
execute_process(
    COMMAND python ${CMAKE_CURRENT_SOURCE_DIR}/tools/install-deps.py
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

project(
    PROJECT_NAME_HERE ## CHANGE ME!!
    VERSION 0.1.0
    LANGUAGES CXX
)

## Find Source Files

## NEED TO ADD A METHOD OF GLOBING FILES IN A PYTHON SCRIPT OR ADD THEM IDIVIDUALLY!!!

## Find Conan Dependencies

## ADD FIND_PACKAGE(X) FOR YOUR CONAN DEPENDENCIES!!!

## Create Engine Shared Library

# add_library(
#     UnifyEngine
#     SHARED
#     #${UNIFY_ENGINE_SOURCES}
# )

## Create Editor Executable

# add_executable(
#     UnifyEditor
#     #${UNIFY_EDITOR_SOURCES}
#     ${CMAKE_CURRENT_SOURCE_DIR}/UnifyEditor/src/main.cpp
# )

## Add Engine Include Directories

# target_include_directories(
#     UnifyEngine
#     PRIVATE
# )

## Add Editor Include Directories

# target_include_directories(
#     UnifyEditor
#     PRIVATE
# )

## Link Dependencies to Engine

# target_link_libraries(
#     UnifyEngine
#     PRIVATE
# )

## Link Depencencies to Editor

# target_link_libraries(
#     UnifyEditor
#     PRIVATE
# )