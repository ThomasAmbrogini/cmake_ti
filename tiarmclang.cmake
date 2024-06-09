# the name of the target operating system
set(CMAKE_SYSTEM_NAME Generic)

# which compilers to use for C and C++
set(CMAKE_C_COMPILER   /opt/ti-cgt-armllvm_3.2.2.LTS/bin/tiarmclang)
set(CMAKE_CXX_COMPILER /opt/ti-cgt-armllvm_3.2.2.LTS/bin/tiarmclang)

# where is the target environment located
set(CMAKE_FIND_ROOT_PATH /opt/ti-cgt-armllvm_3.2.2.LTS/)

set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)

