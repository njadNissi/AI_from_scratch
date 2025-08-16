from email.message import EmailMessage
import os
import smtplib
import ssl
# my google password for python ===> # xuoq pgpy ihev dbxg

sender_email = 'njadnissi@gmail.com'
sender_password = os.environ.get('PYGMAIL')
print(sender_email + ' ' + sender_password)
receiver_email = '3507497566@qq.com'
# receiver_email = '2964142243@qq.com'
# receiver_email = '584162285@qq.com'  # ginias
# receiver_email = '3100884808@qq.com'  # 李想

msg = EmailMessage()
msg['Subject'] = 'NJAD trying python for GMAIL'
msg['From'] = sender_email
msg['To'] = receiver_email
body = html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.baidu.com">link</a> you wanted.
    </p>
  </body>
</html>
"""
msg.set_content(body)

context = ssl.create_default_context()

print('sending...')

with smtplib.SMTP_SSL('smtp.gmail.com', 587, context=context) as smtp:
    smtp.login(sender_email, sender_password)
    smtp.sendmail(sender_email, receiver_email, msg.as_string())

print('success')
