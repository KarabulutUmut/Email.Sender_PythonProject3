import os
import smtplib
from email.message import EmailMessage
import imghdr

def email_Count(filename="email_count.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            count = file.read()
            if count.isdigit():
                count = int(count)
            else:
                count = 0
    else:
        count = 0

    count += 1

    with open(filename, "w") as file:
        file.write(str(count))


host = "smtp-mail.outlook.com"
port = 587

from_email = "umutkarabulut.personal@outlook.com"
to_email = "umutkarabulut.personal@gmail.com"
# getpass could be use for more security, but then program needs to be runned by terminal
password = input("Enter password: ")

msg = EmailMessage()
msg['Subject'] = 'Appointment Found!'
msg['From'] = from_email
msg['To'] = to_email
msg.set_content('Available appointment was found. You snooze, you lose!')

images = ['C:\\Pycharm Projects\\Email Sender\\images\\firstcomefirstserve.jpg',
          'C:\\Pycharm Projects\\Email Sender\\images\\appointmentreminder.png']
for img in images:
    with open(img, 'rb') as image:
        file_data = image.read()
        file_type = imghdr.what(image.name)
        file_name = image.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP(host, port) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(from_email, password)
    server.send_message(msg)

email_Count()
