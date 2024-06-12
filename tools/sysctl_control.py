import subprocess
import json

#$SYSCFG_NODE $SYSCFG_CLI \
#--product $SDK_DIR/.metadata/product.json \
#--context r5fss0-0 \
#--part Default \
#--package ALV \
#--output generated/ \
#./example.syscfg

def read_config_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
command_template = "{SYSCFG_NODE} {SYSCFG_CLI} \
                    --product {SDK_DIR}/.metadata/product.json \
                    --context r5fss0-0 \
                    --part Default \
                    --package ALV \
                    --output ../generated/ \
                    ../{syscfg_file_name}"

if __name__ == "__main__":
    config_file_path = "env_config.json"
    data = read_config_file(config_file_path)

    command = command_template.format(
        SYSCFG_NODE=data["SYSCFG_NODE"],
        SYSCFG_CLI=data["SYSCFG_CLI"],
        SDK_DIR=data["SDK_DIR"],
        syscfg_file_name=data["syscfg_file_name"]
    )

    print(command)

    try:
        result = subprocess.run(command,
                                shell=True,
                                check=True,
                                text=True,
                                capture_output=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

