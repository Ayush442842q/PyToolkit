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

def send_email(sender_email, app_password, recipient, subject, body, attachment=None):
    """Sends an email via Gmail SMTP."""
    if not is_valid_email(sender_email):
        print("❌ Invalid sender email!")
        return False
    if not is_valid_email(recipient):
        print("❌ Invalid recipient email!")
        return False
    try:
        msg = create_message(sender_email, recipient, subject, body)
        if attachment:
            msg = add_attachment(msg, attachment)
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
        print(f"✅ Email sent to {recipient}!")
        return True
    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed! Check your email and app password.")
        return False
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False
