# Day 09 - Email Sender 📧

A Python script to send emails with attachments via Gmail SMTP.

## Features
- 📧 Send single emails via Gmail
- 📎 Attach files to emails
- 📨 Bulk email sending
- 📋 Email log tracking
- ✅ Email validation
- 🔐 Uses Gmail App Password (secure)

## Requirements
- Python 3.6+
- A Gmail account
- Gmail App Password (not your regular password)

## Setup — Gmail App Password
1. Go to Google Account → Security
2. Enable 2-Step Verification
3. Go to App Passwords
4. Generate a new App Password
5. Use that password in the script

## Usage
```bash
python sender.py
```

## Functions
| Function | Description |
|----------|-------------|
| `is_valid_email(email)` | Validates email format |
| `create_message(sender, to, subject, body)` | Creates email object |
| `add_attachment(msg, filepath)` | Attaches file to email |
| `send_email(sender, password, to, subject, body)` | Sends single email |
| `send_bulk_emails(sender, password, recipients, subject, body)` | Sends to multiple |
| `log_email(recipient, subject, status)` | Logs email to file |
| `view_log()` | Displays email log |

## Author
Ayush442842q
