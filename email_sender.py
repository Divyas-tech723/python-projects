import smtplib  #library for sending emails via SMTP(simple mail transfer protocol)
from email.message import EmailMessage  # helps create a well formatted email with sub,body,etc

def send_email(to, subject, body):  
    email = EmailMessage()  #creates a new email object to hold  headers(from,to,subject) and the contents "don't need to create our own class for sending emails.the MIMEMultipart etc,classes provided by python handle everything
    email['From'] = 'your_email ID_here'  
    email['To'] = to  
    email['Subject'] = subject  
    email.set_content(body)  # if you want HTML emails later you can use set_content(body,subtype='html') "an html email is an email that contains html code instead of plain text this allows yy  to format the email like a web page
                         # (mail's outgoing mail server,port for SSL(encrypted connection)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  
        smtp.login('your_email ID_here', 'App_password_here')  
        smtp.send_message(email) #if successful,gmail receives it and delivers to the recevies

# Example usage  
send_email('receiver_email id_here', 'Test Subject', 'Hello, this is a test email!')