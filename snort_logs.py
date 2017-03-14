import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders
import datetime

# Emails snort logs - See snort_bash.sh which is required to create the updates.txt

filepath = '/usr/src/updates.txt'
update_log = open(filepath, 'r')
today = datetime.date.today()
update_read = update_log.read()

fromaddr = "snort@kayos.tech"
toaddr = ["greg@kayos.tech","info@kayos.tech"]

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = ", ".join(toaddr)
msg['Subject'] = "KAOS-IDS-01 - Updates - %s" % (today)
body = "KAOS-IDS-01 Pulled Pork Updates.\n\n %s  \n\n -- netSecure" % update_read
msg.attach(MIMEText(body, 'plain'))
 

filename = "updates.txt"
attachment = open("/usr/src/updates.txt", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('10.1.1.32', 25)
server.starttls()
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
  
update_log.close()
