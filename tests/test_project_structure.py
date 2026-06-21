import os

required_folders = [
    "notebooks",
    "config",
    "deployment",
    "tests",
    "resources"
]

for folder in required_folders:

    if not os.path.isdir(folder):
        raise Exception(
            f"{folder} folder missing"
        )

print(
    "Project Structure Validation Passed"
)
