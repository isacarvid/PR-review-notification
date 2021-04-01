import os

def main():
    file_path = os.environ["INPUT_FILEPATH"]
    username = os.environ["INPUT_USERNAMESECRET"]
    pwd = os.environ["INPUT_PASSWORDSECRET"]


    print(pwd)
    print(username)
    my_output = f"hejhej{file_path}"
    '''lines = open("README.md").readlines
    my_output = lines[0]
    for i in range(lines):
        if lines[i] == "##Members":
            my_output = "yessssss" '''
    print("hej")
    print(file_path.splitlines())
    readme = []
    for file in file_path.splitlines():
        if file.find("README") != -1:
            readme = open(file).readlines() 
    print(readme[0])
    

if __name__ == "__main__":
    main()
