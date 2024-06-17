cmake_minimum_required(VERSION 3.10)

project(hello_world
    DESCRIPTION "CMake Texas R5 Hello World"
    LANGUAGES C)

# Compilation flags
add_library(compilerFlags INTERFACE)
target_compile_options(compilerFlags INTERFACE -mcpu=cortex-r5 -mfloat-abi=hard
                       -mfpu=vfpv3-d16 -mthumb -Wall -Werror -g
                       -Wno-gnu-variable-sized-type-not-at-end
                       -Wno-unused-function -Os)

add_library(compilerDefinitions INTERFACE)
target_compile_definitions(compilerDefinitions INTERFACE SOC_AM64X)

add_library(includeDirectories INTERFACE)
target_include_directories(includeDirectories
                            INTERFACE /opt/ti-cgt-armllvm_3.2.2.LTS/include/c
                            INTERFACE /home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/source
                            INTERFACE /home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/source/kernel/freertos/FreeRTOS-Kernel/include
                            INTERFACE /home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/source/kernel/freertos/portable/TI_ARM_CLANG/ARM_CR5F 
                            INTERFACE /home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/source/kernel/freertos/config/am64x/r5f 
                            INTERFACE generated)

set(SOURCES
    ${PROJECT_NAME}.c
    main.c
)

add_library(linkerFlags INTERFACE)
target_link_directories(linkerFlags INTERFACE
    "/home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/source/board/lib/"
    "/home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/source/drivers/lib/"
    "/home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/source/kernel/freertos/lib/"
    "/opt/ti-cgt-armllvm_3.2.2.LTS/lib/"
)

target_link_options(linkerFlags INTERFACE 
    "-Wl,--diag_suppress=10063"
    "-Wl,--ram_model"
    "-Wl,--reread_libs"
    "-Wl,-m=${PROJECT_NAME}.map"
)
target_link_libraries(linkerFlags INTERFACE 
    "freertos.am64x.r5f.ti-arm-clang.release.lib"
    "drivers.am64x.r5f.ti-arm-clang.release.lib"
    "board.am64x.r5f.ti-arm-clang.release.lib"
    "libc"
    "libsysbm"
    "${CMAKE_SOURCE_DIR}/generated/linker.cmd")

add_subdirectory(generated)

add_executable(${PROJECT_NAME} ${SOURCES})
target_link_libraries(${PROJECT_NAME} PUBLIC lib_generated)
target_link_libraries(${PROJECT_NAME} PUBLIC compilerFlags 
    compilerDefinitions includeDirectories)
target_link_libraries(${PROJECT_NAME} PUBLIC linkerFlags)
