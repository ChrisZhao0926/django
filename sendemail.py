from email.mime.text import MIMEText
from email.header import Header
import smtplib

FROM_ADDR = 'SG-CNBJ-omv-tools-git-G@sonymobile.com'
SMTP_SERVER = 'smtpem1.sonyericsson.net'
TO_ADDR = 'chris.zhao@sonymobile.com'
CC_ADDR = 'DL-CNBJ-FOTA-EMMA-Lab@sonymobile.com'

msg = MIMEText('Hello, just confirm receive mail by DL , please ignore', 'plain', 'utf-8')
msg['From'] = 'SG-CNBJ-omv-tools-git-G'
msg['To'] = Header('Chris')
msg['Cc'] = 'DL-CNBJ-FOTA-EMMA-Lab@sonymobile.com'

msg['Subject'] = '[Test]Python email'

server = smtplib.SMTP(SMTP_SERVER, 25)

server.sendmail(FROM_ADDR, [TO_ADDR, CC_ADDR], msg.as_string())
server.quit()
