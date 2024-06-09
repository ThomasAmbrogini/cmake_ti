#!/bin/bash

SYSCFG_DIR=$HOME/dev/ti/sysconfig/sysconfig_1.20.0/
SDK_DIR=$HOME/dev/ti/am64x/sdk/mcu_plus_sdk_am64x_09_02_01_05/

SYSCFG_NODE=$SYSCFG_DIR/nodejs/node
SYSCFG_CLI=$SYSCFG_DIR/dist/cli.js

$SYSCFG_NODE $SYSCFG_CLI \
--product $SDK_DIR/.metadata/product.json \
--context r5fss0-0 \
--part Default \
--package ALV \
--output generated/ \
./example.syscfg

