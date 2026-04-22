import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

# PyToolkit - Day 09
# Tool: Email Sender
# Author: Ayush442842q
# Description: Send emails with attachments via Gmail SMTP

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
LOG_FILE = "email_log.txt"

def is_valid_email(email):
    """Checks if an email address is valid."""
    return "@" in email and "." in email.split("@")[-1]

def create_message(sender, recipient, subject, body):
    """Creates a basic email message."""
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    return msg

def add_attachment(msg, filepath):
    """Attaches a file to an email message."""
    if not os.path.exists(filepath):
        print(f"❌ Attachment not found: {filepath}")
        return msg
    with open(filepath, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={os.path.basename(filepath)}"
    )
    msg.attach(part)
    print(f"📎 Attached: {os.path.basename(filepath)}")
    return msg
