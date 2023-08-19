import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email information
sender_email = '1234charleswine@gmail.com'
receiver_email = 'harshaltawade405@gmail.com'
subject = 'Drowsiness Alert'
body = 'Driver is Feeling Drowsy!!!'

# Create a multipart message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Add body to the email
message.attach(MIMEText(body, 'plain'))

# SMTP server and port
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Establish a secure connection with the SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# Login to your email account
username = '1234charleswine@gmail.com'
password = 'hylqbjdfmgdzbidb'
server.login(username, password)

# Send the email
server.sendmail(sender_email, receiver_email, message.as_string())

# Close the SMTP server connection
server.quit()

print("Email sent successfully!")
