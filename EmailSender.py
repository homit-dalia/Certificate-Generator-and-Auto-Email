from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

sender = '9898dalia@gmail.com'
receiver = 'homitdalia72@gmail.com'

msg = MIMEMultipart()

msg['Subject'] = 'Test mail with attachment'
msg['From'] = sender
msg['To'] = receiver
