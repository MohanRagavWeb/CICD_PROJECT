import os

required_folders = [
    "notebooks",
    "config",
    "deployment",
    "tests"
]

for folder in required_folders:

    if not os.path.exists(folder):
        raise Exception(
            f"{folder} missing"
        )

print("All tests passed")
