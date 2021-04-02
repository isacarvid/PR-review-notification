import os

def emailFinder(readme):
    num_email = 0
    mails = []

    for line in readme:
        domain_index = 0
        start_index = 0
        while domain_index < len(line):
            domain_index = line.find('@kth.se', domain_index)
            if domain_index == -1:
                break

            num_email += 1
            start_index = domain_index
            while len(mails) != num_email and start_index >= 0:
                if line[start_index] == ' ':
                    start_index += 1
                    mails.append(line[start_index:domain_index+6])
                    break
                start_index -= 1
            
            domain_index += 7 # 7 is len("@kth.se")
        return (num_email, mails)

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
    
    notify = False
    for line in readme:
        if "notify" in line:
            notify = True
            break

    if notify:
        (num_mail, mails) = emailFinder(readme)
        for mail_addr in mails:
            # send to each mail
            1 == 1

if __name__ == "__main__":
    main()
