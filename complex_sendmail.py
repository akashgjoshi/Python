import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

username="akashgjoshi@gmail.com"
passwd="!Shobha4"
#passwd for pythonshishya@gmail is gopalkrishna
fromaddr="akashgjoshi@gmail.com"
toaddr="akashgjoshi@gmail.com"
msg=MIMEMultipart()
msg['From']=fromaddr
msg['To']=toaddr
msg['Subject']="Image with email"
img_dir="C:\\Users\\ankan_000\\Desktop\\pp.jpg"

file=open(img_dir,'rb').read()
img=MIMEImage(file,name=os.path.basename(img_dir))
msg.attach(img)	

body="I am sending this mail through a Python script I am writing.\n Let me know if you receive the mail."
msg.attach(MIMEText(body,'plain'))
html="""\
<html>
<head></head>
<body bgcolor="Orange">
<p>
Hello. How are you? <br>Please visit us at <a href="www.tradeweb.com"><b>Tradeweb</b></a>
</p>
</body>
</html>
"""
msg.attach(MIMEText(html,'html'))

server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(username,passwd)
txt=msg.as_string()
server.sendmail(fromaddr,toaddr,txt)

server.quit()



