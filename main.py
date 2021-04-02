import os
import smtplib, ssl

def sendEmail(username, password, domain, toAddress, msg):
    port = 465
    context = ssl.create_default_context()
    server = ""

    with smtplib.SMTP_SSL(domain, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, toAddress, msg)


def main():
    file_path = os.environ["INPUT_FILEPATH"]
    username = os.environ["INPUT_USERNAMESECRET"]
    pwd = os.environ["INPUT_PASSWORDSECRET"]
    domain = os.environ["INPUT_DOMAINSECRET"]

    message = """\
        Subject: Kth devops

        You recieved a comment on your PR."""
    readme = []
    for file in file_path.splitlines():
        if file.find("README") != -1:
            readme = open(file).readlines() 
    sendEmail(username, pwd, domain, username, message)
    

if __name__ == "__main__":
    main()
