import smtplib
from email.message import EmailMessage  

def send_email(to, subject, body):  
    email = EmailMessage()  
    email['From'] = 'your_email ID_here'  
    email['To'] = to  
    email['Subject'] = subject  
    email.set_content(body)  
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  
        smtp.login('your_email ID_here', 'App_password_here')  
        smtp.send_message(email) 

send_email('receiver_email id_here', 'Test Subject', 'Hello, this is a test email!')
