#Import SMTPLIB
import smtplib
from email.mime.text import MIMEText
host="smtp.gmail.com"
port=587
from_email="pythonshishya@gmail.com"
to=["akashgjoshi@gmail.com"]
username="pythonshishya@gmail.com"
passwd="gopalkrishna"
conn=smtplib.SMTP(host,port)
conn.ehlo()
conn.starttls()
conn.login(username,passwd)
msg="Hello,\n How are you?"
conn.sendmail(from_email,to,msg)
conn.quit()