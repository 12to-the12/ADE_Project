
debugging = True

def p(message):
    if debugging: print(message)
p('<START>')
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
p('imports completed')

#Setup the MIME
def send_email(body='this is a test email',subject='a message', 
sender_address = 'sageisthyname@gmail.com', sender_pass = 'mkvlifersccmxmkk', 
receiver_address='loganthomashillyer@gmail.com',):
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject
    #The body and the attachments for the mail
    message.attach(MIMEText(body, 'plain'))
    p('message built')
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    p('session started')
    session.starttls() #enable security
    p('session secured')
    session.login(sender_address, sender_pass) #login with mail_id and password
    p('logged in')
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    p('message sent')
    session.quit()
    print('session terminated')

send_email()

p('<END>')