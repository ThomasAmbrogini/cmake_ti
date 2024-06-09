cmake_minimum_required(VERSION 3.10)

project("CMake Texas R5 Hello World")

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

add_library(hello_world OBJECT hello_world.c)
target_link_libraries(hello_world compilerFlags compilerDefinitions
                      includeDirectories)

add_library(driversConfig OBJECT generated/ti_drivers_config.c)
target_link_libraries(driversConfig compilerFlags compilerDefinitions
                      includeDirectories)

add_library(driversOpenClose OBJECT generated/ti_drivers_open_close.c)
target_link_libraries(driversOpenClose compilerFlags compilerDefinitions
                      includeDirectories)

add_library(boardConfig OBJECT generated/ti_board_config.c)
target_link_libraries(boardConfig compilerFlags compilerDefinitions
                      includeDirectories)

add_library(boardOpenClose OBJECT generated/ti_board_open_close.c)
target_link_libraries(boardOpenClose compilerFlags compilerDefinitions
                      includeDirectories)

add_library(dplConfig OBJECT generated/ti_dpl_config.c)
target_link_libraries(dplConfig compilerFlags compilerDefinitions
                      includeDirectories)

add_library(pinmuxConfig OBJECT generated/ti_pinmux_config.c)
target_link_libraries(pinmuxConfig compilerFlags compilerDefinitions
                      includeDirectories)

add_library(powerClockConfig OBJECT generated/ti_power_clock_config.c)
target_link_libraries(powerClockConfig compilerFlags compilerDefinitions
                      includeDirectories)



# Linking
# /opt/ti-cgt-armllvm_3.2.2.LTS/bin/tiarmclang   -Wl,--diag_suppress=10063 -Wl,--ram_model -Wl,--reread_libs   -Wl,-i/home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_
# 01_05/source/kernel/freertos/lib -Wl,-i/home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/source/drivers/lib -Wl,-i/home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am
# 64x_09_02_01_05/source/board/lib -Wl,-i/opt/ti-cgt-armllvm_3.2.2.LTS/lib   -Wl,-m=hello_world.release.map -o hello_world.release.out obj/release/hello_world.obj obj/relea
# se/main.obj obj/release/ti_drivers_config.obj obj/release/ti_drivers_open_close.obj obj/release/ti_board_config.obj obj/release/ti_board_open_close.obj obj/release/ti_dpl
# _config.obj obj/release/ti_pinmux_config.obj obj/release/ti_power_clock_config.obj -lfreertos.am64x.r5f.ti-arm-clang.release.lib -ldrivers.am64x.r5f.ti-arm-clang.release.
# lib -lboard.am64x.r5f.ti-arm-clang.release.lib -llibc.a -llibsysbm.a   generated/linker.cmd  
# Add executable target

add_library(linkerFlags INTERFACE)
target_link_directories(linkerFlags INTERFACE 
    /home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/source/kernel/freertos/lib
    /home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/source/drivers/lib
    /home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/source/board/lib
    /opt/ti-cgt-armllvm_3.2.2.LTS/lib
)
target_link_libraries(linkerFlags INTERFACE
    libc
    libsysbm
    freertos.am64x.r5f.ti-arm-clang.release.lib
    drivers.am64x.r5f.ti-arm-clang.release.lib
    board.am64x.r5f.ti-arm-clang.release.lib
)

add_executable(hello_world.release main.c)
target_link_libraries(hello_world.release PUBLIC compilerFlags 
    compilerDefinitions includeDirectories)
target_link_libraries(hello_world.release PUBLIC hello_world driversConfig
    driversOpenClose boardConfig boardOpenClose dplConfig pinmuxConfig
    powerClockConfig)

target_link_libraries(hello_world.release PUBLIC linkerFlags)

# Specify linker options for the executable target
target_link_options(hello_world.release PUBLIC 
    "-Wl,--diag_suppress=10063"
    "-Wl,--ram_model"
    "-Wl,--reread_libs"
    "-Wl,-i/home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/source/kernel/freertos/lib"
    "-Wl,-i/home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/source/drivers/lib"
    "-Wl,-i/home/thomas/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/source/board/lib"
    "-Wl,-i/opt/ti-cgt-armllvm_3.2.2.LTS/lib"
    "-Wl,-m=hello_world.release.map"
)

# Include the linker command file
target_link_options(hello_world.release PUBLIC 
    "-Tgenerated/linker.cmd"
)

