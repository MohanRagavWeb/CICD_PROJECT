import os

required_files = [

    "config/dev_config.ipynb",
    "config/test_config.ipynb",
    "config/prod_config.ipynb"

]

for file in required_files:

    if not os.path.exists(file):
        raise Exception(
            f"{file} missing"
        )

print(
    "Config Validation Passed"
)
