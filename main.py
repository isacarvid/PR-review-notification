import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    yaml_path = os.environ["INPUT_PATH"]
    file_path = os.environ["INPUT_FILEPATH"]

    my_output = f"hejhej{file_path}"
    lines = open("README.md").readlines
    my_output = lines[0]
    for i in range(lines):
        if lines[i] == "##Members":
            my_output = "yessssss" 
    print(f"::set-output name=myOutput::{my_output}")

if __name__ == "__main__":
    main()
