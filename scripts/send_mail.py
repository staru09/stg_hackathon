import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
import os
import schedule
import time

def send_email_with_attachment():
    sender_email = ""
    receiver_email = ""
    subject = "Daily Excel Report"
    body = "Please find the attached Excel report for the day."
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_password = ""

    file_path = r"C:\Users\91745\OneDrive\Desktop\stg_hackathon\utils\Audit_report.xlsx"
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    attachment = MIMEBase("application", "octet-stream")
    with open(file_path, "rb") as file:
        attachment.set_payload(file.read())

    encoders.encode_base64(attachment)
    attachment.add_header(
        "Content-Disposition", f"attachment; filename= {os.path.basename(file_path)}"
    )
    msg.attach(attachment)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, smtp_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print(f"Email sent to {receiver_email} with attachment.")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

schedule.every().day.at("07:56").do(send_email_with_attachment)

while True:
    schedule.run_pending()
    time.sleep(60)
