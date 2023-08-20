import smtplib
from email.mime.text import MIMEText

sender = ""
recipients = "[]"

subject = "Subject goes here"

with open("body.txt", 'r') as bodyFile:
    body = bodyFile.read()

with open("password.txt", 'r') as passwordFile:
    password = passwordFile.read()

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)
