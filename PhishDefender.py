import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass
import csv
import time

# Function to send a phishing email
def send_phishing_email(sender_email, recipient_email, password, phishing_link):
    # Create an SMTP connection to Gmail's server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    # Define the email content
    subject = "Important Password Reset"
    from_name = "IT Support"
    to_name = "Employee"
    body = f"Please click the link below to reset your password:\n{phishing_link}"
    msg = MIMEMultipart()
    msg["From"] = from_name
    msg["To"] = to_name
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Send the phishing email
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

# Function to log phishing attempts
def log_attempt(attempt_log, recipient_email, timestamp, response):
    # Open the attempt log file in append mode
    with open(attempt_log, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Write the attempt details to the CSV file
        writer.writerow([timestamp, recipient_email, response])

# Simulated phishing parameters
sender_email = "your_email@gmail.com"
password = getpass("Enter your email password: ")  # Securely input the password
phishing_link = "https://phishinglink.com/reset"

# Create an attempt log file (or specify an existing one)
attempt_log = "phishing_attempts.csv"

try:
    while True:
        recipient_email = input("Enter recipient's email: ")
        send_phishing_email(sender_email, recipient_email, password, phishing_link)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        response = input("Did the recipient click the link? (yes/no): ")
        log_attempt(attempt_log, recipient_email, timestamp, response)
except KeyboardInterrupt:
    print("Phishing simulation ended.")
