import argparse
import json
import subprocess


cli_template = "{SYSCFG_NODE} {SYSCFG_CLI} \
        --product {SDK_DIR}/.metadata/product.json \
        --context r5fss0-0 \
        --part Default \
        --package ALV \
        --output ../generated/ \
        ../{syscfg_file_name}"


gui_template = "{SYSCFG_GUI} \
        --product {SDK_DIR}/.metadata/product.json \
        --context r5fss0-0 \
        --part Default \
        --package ALV \
        ../{syscfg_file_name}"


def read_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def populate_template(mode, data):
    if mode == "gui":
        command = gui_template.format(
            SYSCFG_GUI=data["SYSCFG_GUI"],
            SDK_DIR=data["SDK_DIR"],
            syscfg_file_name=data["syscfg_file_name"]
        )
    else:
        command = cli_template.format(
            SYSCFG_NODE=data["SYSCFG_NODE"],
            SYSCFG_CLI=data["SYSCFG_CLI"],
            SDK_DIR=data["SDK_DIR"],
            syscfg_file_name=data["syscfg_file_name"]
        )

    return command


if __name__ == "__main__":
    config_file_path = "env_config.json"

    parser = argparse.ArgumentParser(description="Run sysconfig in \
            gui mode or to generate the configuration files")
    parser.add_argument("--mode", required=True, help="gui or cli")
    parser.add_argument("--env_file", required=False, help="name of the \
            json configuration file of the environment")

    args = parser.parse_args()

    if args.env_file is not None:
        config_file_path = args.env_file

    data = read_file(config_file_path)

    command = populate_template(args.mode, data)

    try:
        result = subprocess.run(command,
                                shell=True,
                                check=True,
                                text=True,
                                capture_output=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)
