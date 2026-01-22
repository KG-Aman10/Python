import smtplib
from email.message import EmailMessage

email = input("Enter your Email: ")
app_password = input("Enter your App Password: ")
subject = input("Enter the Subject: ")
body = input("Enter the Body: ")

recipients = [
    "amanpatidar874@gmail.com",
    "amanpatidar045@gmail.com"
]

msg = EmailMessage()
msg["From"] = email
msg["To"] = ", ".join(recipients)
msg["Subject"] = subject
msg.set_content(body)

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, app_password)
    server.send_message(msg)
    print("✅ Email sent successfully!")

except Exception as e:
    print("❌ Error:", e)

finally:
    if server:
        server.quit()
