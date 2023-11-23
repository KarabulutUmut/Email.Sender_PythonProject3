import getpass
import smtplib
from email.message import EmailMessage
import imghdr


HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "umutkarabulut.personal@outlook.com"
TO_EMAIL = "mage9898@outlook.com"
PASSWORD = getpass.getpass("Enter password: ")

msg = EmailMessage()
msg['Subject'] = 'Appointment Found!'
msg['From'] = FROM_EMAIL
msg['To'] = TO_EMAIL
msg.set_content('Available appointment was found. You snooze, you lose!')

images = ['C:\\Pycharm Projects\\emailsender\\images\\firstcomefirstserve.jpg',
          'C:\\Pycharm Projects\\emailsender\\images\\appointmentreminder.png']
for img in images:
    with open(img, 'rb') as image:
        file_data = image.read()
        file_type = imghdr.what(image.name)
        file_name = image.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP(HOST, PORT) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(FROM_EMAIL, PASSWORD)
    server.send_message(msg)