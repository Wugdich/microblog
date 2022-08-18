from flask_mail import Message
from app import mail


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

