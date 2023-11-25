import smtplib
from email.message import EmailMessage
import imghdr


host = "smtp-mail.outlook.com"
port = 587

from_email = "umutkarabulut.personal@outlook.com"
to_email = "umutkarabulut.personal@gmail.com"
password = input("Enter password: ")

msg = EmailMessage()
msg['Subject'] = 'Appointment Found!'
msg['From'] = from_email
msg['To'] = to_email
msg.set_content('Available appointment was found. You snooze, you lose!')

images = ['C:\\Pycharm Projects\\emailsender\\images\\firstcomefirstserve.jpg',
          'C:\\Pycharm Projects\\emailsender\\images\\appointmentreminder.png']
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