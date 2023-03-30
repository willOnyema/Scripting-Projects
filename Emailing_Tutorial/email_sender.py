import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
personal_email = 'wonyema@gmail.com'
email = EmailMessage()
email['from'] = 'William Onyema'
email['to'] = personal_email
email['subject'] = 'You\'ve won a 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:
    email_address = 'joldin7@gmail.com'
    email_password = 'nprhxvvkhfipvwyq'
    smtp.login(email_address, email_password)
    smtp.send_message(email)
    smtp.sendmail(from_addr=email_address, to_addrs=personal_email, msg="subject:hi \n\n this is my message")
    print('all good boss')
