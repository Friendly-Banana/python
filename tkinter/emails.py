#!/usr/bin/python3
import smtplib
import ssl
from email.message import EmailMessage

from email import message_from_bytes
from imaplib import IMAP4_SSL
from tkinter import Message

port = 465  # For SSL

# Create a secure SSL context
context = ssl.create_default_context()


def send_email(sender, password, text, subject, recipient):
    msg = EmailMessage()
    msg.set_content(text)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    try:
        # log into server and send email
        with smtplib.SMTP_SSL("mail.gmx.de", port, context=context) as server:
            server.login(msg["From"], password)
            server.sendmail(msg["From"], msg["To"], msg.as_string())
    except smtplib.SMTPAuthenticationError:
        return "Invalid Credentials"
    except smtplib.SMTPException as e:
        return e
    return "OK"


def new_emails(email, password, subject="Tkinter Chat") -> "list[Message]":
    new_msgs = []
    with IMAP4_SSL("imap.gmx.de") as server:
        server.login(email, password)
        server.select("INBOX")
        (retcode, messages) = server.search(None, f'(UNSEEN SUBJECT "{subject}")')
        if retcode == "OK" and messages[0]:
            for index, num in enumerate(messages[0].split()):
                typ, data = server.fetch(num, "(RFC822)")
                message = message_from_bytes(data[0][1])
                typ, data = server.store(num, "+FLAGS", "\\Seen")
                new_msgs.append(message)

    return new_msgs