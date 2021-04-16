import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

#login to the account with encrypted pasword
with open('password.txt', 'r') as f:
    password = f.read()
    
server.login('mail@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'DesignIsOrion'
msg['To'] = 'Test@mail.com'
msg['Subject'] = 'Just a Subject'

# Sending the message which is on another file called message.txt
with open('message.txt', r) as f:
    message = f.read()
    
msg.attach(MIMEText(message, 'plain'))

# Attachment of image
filename = 'coding.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachement.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachement; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('mail@gmail.com', 'Test@mail.com', text)
