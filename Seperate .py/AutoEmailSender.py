from email.message import EmailMessage
import ssl
import smtplib

receiver='homitdalia72@gmail.com'
sender='9898dalia@gmail.com'
password='nkzgyfdoviqzpwje'

subject = "Webinar E-Certificate"
body = """ Dear Participant,
                       Congratulations for successfully attending an ISTE approved webinar on “Deep Learning using Python” on 17th September, 2021, organized by CO, CKPCET.

Regards,
Webinar Coordinator

"""


em = EmailMessage()
em['From']=sender
em['To']=receiver
em['Subject']=subject
em.set_content(body)

filename = 'PPT.pdf'
with open(filename, 'r') as f:
    part = MIMEApplication(f.read(), Name=basename(filename))

part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
em.attach(part)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender,password)
    smtp.sendmail(sender,receiver,em.as_string())
