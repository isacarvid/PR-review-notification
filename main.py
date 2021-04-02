import os
import smtplib, ssl

def sendEmail(username, password, domain, toAddress, msg):
    port = 465
    context = ssl.create_default_context()
    server = ""

    with smtplib.SMTP_SSL(domain, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, toAddress, msg)


def emailFinder(readme, domain):
    addr_suffix = "@"+domain
    num_email = 0
    mails = []

    for line in readme:
        addr_suffix = "@"+domain
        domain_index = 0
        start_index = 0
        while domain_index < len(line):
            domain_index = line.find(addr_suffix, domain_index)
            if domain_index == -1:
                break

            num_email += 1
            start_index = domain_index
            while len(mails) != num_email and start_index >= 0:
                if line[start_index] == ' ':
                    mails.append(line[start_index+1:domain_index+len(addr_suffix)])
                    break
                if start_index == 0:
                    mails.append(line[start_index:domain_index+len(addr_suffix)])
                    break
                start_index -= 1
            
            domain_index += len(addr_suffix)
            
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
        mails = emailFinder(readme, "kth.se")
        mails += emailFinder(readme, "gmail.com") # for debug
        for to_addr in mails:
            sendEmail(username, pwd, domain, to_addr, message)


if __name__ == "__main__":
    main()
