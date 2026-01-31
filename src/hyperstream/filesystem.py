from pathlib import Path


def write(file_name: str | Path, content: str) -> None:
    with open(file_name, "w+") as file:
        _ = file.write(content)


def read(file_name: str | Path) -> str:
    with open(file_name, "r+") as file:
        return file.read()
