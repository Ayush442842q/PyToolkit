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
