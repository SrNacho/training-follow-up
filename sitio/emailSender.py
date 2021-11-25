# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

def sendEmail(email, code, token):
    message = Mail(
        from_email='noreply-trainingfollowup@yopmail.com',
        to_emails=email,
        subject='Password change',
        html_content='Your password verification code is <strong>{}</strong>'.format(code))
    try:
        sg = SendGridAPIClient(token)
        response = sg.send(message)
    except Exception as e:
        print(e)