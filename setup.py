from setuptools import setup

setup(
    name="tasks",
    version="1.0",
    py_modules=["task_cli"],
    entry_points={
        "console_scripts": [
            "tasks=task_cli:main",
        ],
    },
)