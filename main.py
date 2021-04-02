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
    domain = os.environ["INPUT_DOMAINSECRET"]

    message = """\
        Subject: Kth devops

        You recieved a comment on your PR."""
    readme = []
    for file in file_path.splitlines():
        if file.find("README") != -1:
            readme = open(file).readlines() 

    notify = False
    for line in readme:
        if "notify" in line:
            notify = True
            break

    if notify:
        (num_mail, mails) = emailFinder(readme)
        for to_addr in mails:
            sendEmail(username, pwd, domain, to_addr, message)


if __name__ == "__main__":
    main()
