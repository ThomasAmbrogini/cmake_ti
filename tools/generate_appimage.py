import argparse

HOME = "/home/thomas"
SDK_DIR = "HOME/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/"

SYSCFG_DIR="HOME/dev/ti/sysconfig/sysconfig_1.20.0/"
SYSCFG_NODE=$SYSCFG_DIR/nodejs/node
SYSCFG_CLI=$SYSCFG_DIR/dist/cli.js

XIPGEN_CMD=$SDK_DIR/tools/boot/xipGen/xipGen.out
OUTRPRC_CMD="$SYSCFG_NODE $SDK_DIR/tools/boot/out2rprc/elf2rprc.js"
MULTI_CORE_IMAGE_GEN="$SYSCFG_NODE $SDK_DIR/tools/boot/multicoreImageGen/multicoreImageGen.js"
APP_IMAGE_SIGN_CMD=$SDK_DIR/tools/boot/signing/appimage_x509_cert_gen.py


OUTNAME=build_separate_generated/hello_world.release.out
BOOTIMAGE_NAME=hello_world.release.appimage
BOOTIMAGE_NAME_XIP=hello_world.release.appimage_xip
BOOTIMAGE_NAME_SIGNED=hello_world.release.appimage.signed
BOOTIMAGE_RPRC_NAME=hello_world.release.rprc
BOOTIMAGE_RPRC_NAME_XIP=hello_world.release.rprc_xip
BOOTIMAGE_RPRC_NAME_TMP=hello_world.release.rprc_tmp
BOOTIMAGE_NAME_HS=hello_world.release.appimage.hs
BOOTIMAGE_NAME_HS_FS=hello_world.release.appimage.hs_fs

BOOTIMAGE_CORE_ID_a53ss0_0=0
BOOTIMAGE_CORE_ID_r5fss0_0=4
BOOTIMAGE_CORE_ID_r5fss0_1=5
BOOTIMAGE_CORE_ID_r5fss1_0=6
BOOTIMAGE_CORE_ID_r5fss1_1=7
BOOTIMAGE_CORE_ID_m4fss0_0=14
SBL_RUN_ADDRESS=0x70000000
SBL_DEV_ID=55

MULTI_CORE_IMAGE_PARAMS=$BOOTIMAGE_RPRC_NAME@$BOOTIMAGE_CORE_ID_r5fss0_0
MULTI_CORE_IMAGE_PARAMS_XIP=$BOOTIMAGE_RPRC_NAME_XIP@$BOOTIMAGE_CORE_ID_r5fss0_0

APP_SIGNING_KEY=$SDK_DIR/tools/boot/signing/app_degenerateKey.pem

BOOTIMAGE_TEMP_OUT_FILE=temp_stdout_release.txt


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()

    
