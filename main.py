import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    yaml_path = os.environ["INPUT_PATH"]
    my_input = os.environ["INPUT_MYINPUT"]

    my_output = f"Hello {my_input}"
    lines = open("README.md").readlines
    my_output = lines[0]
    for i in range(lines):
        if lines[i] == "##Members":
            my_output = "yessssss"


        
    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
