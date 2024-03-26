import smtplib
import getpass
from email.message import EmailMessage

message = EmailMessage()
sender = "martin.heinrich91@gmail.com"
recipient = "mila.mutic@gmail.com"
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
body = """PYTHON

Hey there!

I'm learning to send emails using Python!"""
message.set_content(body)

mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_server.set_debuglevel(1)

#mail_pass = getpass.getpass('Password? ')
mail_pass =  'tmcvujgwadfpooqo'

print(mail_pass)

mail_server.login(sender, mail_pass)
mail_server.send_message(message)

# tmcv ujgw adfp ooqo
# tmcvujgwadfpooqo
