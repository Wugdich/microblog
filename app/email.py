from flask_mail import Message
from app import mail
from flask import render_template
from app import app


sender_email = str
recipient_email = str
raw_html_string = str


def send_email(subject: str,
               sender: sender_email,
               recipients: list[recipient_email],
               text_body: str,
               html_body: raw_html_string) -> None:
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Yout Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))
        
