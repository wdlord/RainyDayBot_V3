import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# sends an SMS message using an email gateway
def send_message(subject_line, body):
  email = os.environ['EMAIL']
  password = os.environ['PASSWORD']
  phone = os.environ['PHONE']

  # this is for t-mobile, different carriers use something different
  sms_gateway = phone + '@tmomail.net'

  # server for sending text over email
  smtp = "smtp.gmail.com"
  port = 587

  # start server and login
  server = smtplib.SMTP(smtp, port)
  server.starttls()
  server.login(email, password)

  # prepare mail fields
  message = MIMEMultipart()
  message['From'] = email
  message['To'] = sms_gateway

  # subject line and body
  message['Subject'] = subject_line

  # we're just sending plain text, attach it to message
  message.attach(MIMEText(body + '\n', 'plain'))

  # send the text over email
  server.sendmail(email, sms_gateway, message.as_string())

  # exit the server
  server.quit()
