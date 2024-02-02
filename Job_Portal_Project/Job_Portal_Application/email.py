
    
from email.message import EmailMessage
import ssl
import smtplib

def send_mail():
    email_sender = "python392002@gmail.com"
    email_password = "dywn rusb nnyn gqvv"
    email_receiver = "python392002@gmail.com"
    subject = "Successfully login you have to search jobs"

    body = """
    Welcome to our Job Portal
    """

    # Corrected: Instantiate the EmailMessage class
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        
        