# Dev Notes - Email Sender

## What I learned
- `smtplib.SMTP(server, port)` — connects to email server
- `server.starttls()` — encrypts the connection (TLS)
- `server.login(email, password)` — authenticates with Gmail
- `MIMEMultipart()` — creates email with multiple parts
- `MIMEText(body, "plain")` — creates plain text email body
- `MIMEBase("application", "octet-stream")` — creates attachment part
- `encoders.encode_base64(part)` — encodes attachment as base64
- `msg.add_header()` — adds metadata to attachment
- App Password vs regular password — always use App Password with Gmail
- SMTP port 587 — standard port for TLS email sending

## Important
- Never hardcode passwords in code
- Use Gmail App Passwords not your main password
- Enable 2FA first before generating App Password
- SMTP port 587 = TLS, port 465 = SSL

## Challenges
- Gmail blocks regular password login for scripts
- Need to enable App Password in Google Account settings
- Always validate email before attempting to send
