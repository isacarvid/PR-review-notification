import os
import smtplib, ssl

def sendEmail(username, password):
    port = 465
    context = ssl.create_default_context()
    server = ""

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(username, password)

    return True

def main():
    file_path = os.environ["INPUT_FILEPATH"]
    username = os.environ["INPUT_USERNAMESECRET"]
    pwd = os.environ["INPUT_PASSWORDSECRET"]
    domain = os.environ["INPUT_DOMAINSECRET"]

    print(pwd)
    print(username)  
    print("hej")
    print(file_path.splitlines())

    readme = []
    for file in file_path.splitlines():
        if file.find("README") != -1:
            readme = open(file).readlines() 
    print(readme[0])
    

if __name__ == "__main__":
    main()
