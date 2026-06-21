import subprocess

test_files = [

    "tests/test_project_structure.py",
    "tests/test_configs.py"

]

for test in test_files:

    result = subprocess.run(
        ["python", test]
    )

    if result.returncode != 0:

        raise Exception(
            f"{test} failed"
        )

print(
    "All Tests Passed"
)
