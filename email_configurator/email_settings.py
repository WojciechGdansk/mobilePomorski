import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from_address = 'from@address.com'
to_address = 'to@address.com'
subject = "some subject"
content = 'tresc wiaodmosci'

msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject
body = MIMEText(content, 'plain')
msg.attach(body)

filename = 'bbb.docx'

with open(filename, 'rb') as f:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")


msg.attach(part)

with smtplib.SMTP('smtp.poczta.onet.pl', 587) as server:
    server.login(from_address, 'password')
    server.send_message(msg, from_addr=from_address, to_addrs=[to_address])
