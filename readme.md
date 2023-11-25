# Email Sender

> This program is for sending emails. Attachements can be included.
> There is a counter to see how many emails have been sent in total.

## For PDF

> For PDF files you have to make a small change:

```
with open('resume.pdf', 'rb') as f:
    file_data = f.read()
    file_name = f.name
msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)