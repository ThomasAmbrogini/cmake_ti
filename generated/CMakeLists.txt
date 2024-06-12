set(SOURCES
    ti_drivers_config.c
    ti_drivers_open_close.c
    ti_board_config.c
    ti_board_open_close.c
    ti_dpl_config.c
    ti_pinmux_config.c
    ti_power_clock_config.c
    ti_power_clock_config.c
)

add_library(lib_generated ${SOURCES})
target_link_libraries(lib_generated PUBLIC compilerFlags 
    compilerDefinitions includeDirectories)
target_link_libraries(lib_generated PUBLIC linkerFlags)

