import os
import smtplib
import getpass
import sys

server = input("Enter Mail Server (e.g., gmail, yahoo): ")
user = input("E-mail Address: ")
passwd = getpass.getpass("Password: ")
to = input("Target E-mail Address: ")
subject = input("Subject: ")
body = input("Body: ")
emails = int(input("Number Of Emails: "))

if server == "gmail":
    smtp_server = "smtp.gmail.com"
    port = 587
elif server == "yahoo":
    smtp_server = "smtp.mail.yahoo.com"
    port = 465
else:
    print("Script supports only Gmail and Yahoo for research purposes.")
    sys.exit()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
        server.starttls()
    server.login(user, passwd)

    for i in range(1, emails + 1):
       # msg = f"From: {user}\\nSubject: {subject}\\n{body}"
        msg = 'From: ' + user + '\nMessage: ' + '\n' + body
        server.sendmail(user, to, msg)
        print(f"Sending Email {i}/{emails}...")

    server.quit()
    print("\\nTarget Email Address Has Been Sent Emails Successfully!")
except KeyboardInterrupt:
    print("\\nCanceled.")
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print("\\nIncorrect Credentials.")
    sys.exit()
