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

def log_email(recipient, subject, status):
    """Logs sent emails to a text file."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"[{timestamp}] To: {recipient} | Subject: {subject} | Status: {status}\n")
    print(f"📝 Email logged!")

def send_bulk_emails(sender_email, app_password, recipients, subject, body):
    """Sends emails to multiple recipients."""
    results = {"success": 0, "failed": 0}
    for recipient in recipients:
        success = send_email(sender_email, app_password, recipient, subject, body)
        if success:
            log_email(recipient, subject, "SUCCESS")
            results["success"] += 1
        else:
            log_email(recipient, subject, "FAILED")
            results["failed"] += 1
    print(f"\n📊 Bulk send complete: {results['success']} sent, {results['failed']} failed")
    return results

def view_log():
    """Displays the email log."""
    if not os.path.exists(LOG_FILE):
        print("❌ No log file found!")
        return
    print("\n📋 Email Log")
    print("-" * 60)
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if not lines:
        print("No emails logged yet.")
    for line in lines:
        print(line.strip())
    print("-" * 60)
    print(f"Total: {len(lines)} emails logged")
