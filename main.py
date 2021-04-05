import os
import smtplib, ssl

def sendEmail(username, password, domain, toAddress, msg):
    port = 465
    context = ssl.create_default_context()
    server = ""

    with smtplib.SMTP_SSL(domain, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, toAddress, msg)


def emailFinder(readme):
    mails = []

    for line in readme:
        addr_prefix = ""
        addr_suffix = ""
        domain_index = 0
        while domain_index < len(line):
            domain_index = line.find("@", domain_index)
            if domain_index == -1: # no emails on this line
                break
            
            start_index = domain_index
            while start_index >= 0:
                if line[start_index] == ' ':
                    start_index += 1
                    break
                if start_index == 0:
                    break
                start_index -= 1
            
            end_index = domain_index
            while end_index < len(line):
                if line[end_index] == ' ':
                    break
                if end_index == len(line)-1:
                    break
                end_index += 1
                
            mails.append(line[start_index:end_index])
            
            domain_index += 1 # 1 is len("@")
            
    return mails

def main():
    file_path = os.environ["INPUT_FILEPATH"]
    username = os.environ["INPUT_USERNAMESECRET"]
    pwd = os.environ["INPUT_PASSWORDSECRET"]
    domain = os.environ["INPUT_DOMAINSECRET"]
    keyword = os.environ["INPUT_KEYWORD"]

    message = """\
        Subject: Kth devops

        You recieved a comment on your PR."""
    readme = []
    for file in file_path.splitlines():
        if file.find("README") != -1:
            readme = open(file).readlines() 

    notify = False
    for line in readme:
        if keyword in line:
            notify = True
            break

    if notify:
        mails = emailFinder(readme)
        for to_addr in mails:
            sendEmail(username, pwd, domain, to_addr, message)


if __name__ == "__main__":
    main()
