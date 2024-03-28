#!/usr/bin/env python3

from email.message import EmailMessage
import mimetypes
import os
import smtplib


def generate_email(sender, recipient, subject, body, attachment_path=None):
    """Creates an email with an optional attachement."""
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = subject
    email.set_content(body)

    if attachment_path:
        # If there is an attachment, Process it and add it to the email
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment_path, 'rb') as ap:
            email.add_attachment(ap.read(),
                                 maintype=mime_type, subtype=mime_subtype,                        filename=attachment_filename)

    return email


def send_email(email):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(email)
    mail_server.quit()
