import os
import smtplib
import csv

os.environ["GMAIL_USERNAME"] = "Your Email"
os.environ["GMAIL_PASSWORD"] = "Your_password"


def send_mass_gmail(email_addresses, email_body, subject):
  # Connect to the SMTP server
  smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
  smtp_server.starttls()
  smtp_server.login(os.environ.get("GMAIL_USERNAME"),
                    os.environ.get("GMAIL_PASSWORD"))
  # Send the email to each recipient
  for email_address in email_addresses:
    message = 'Subject: {}\n\n{}'.format(subject, email_body)
    smtp_server.sendmail(os.environ.get("GMAIL_USERNAME"), email_address,
                         message)
  # Close the connection to the SMTP server
  smtp_server.quit()


if __name__ == "__main__":
  # Read the email addresses from a CSV file
  with open('email_addresses.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    email_addresses = [row[0] for row in reader]
  # Read the email body from a text file
  with open('email_body.txt', 'r') as txtfile:
    email_body = txtfile.read()
  # Send the email
  send_mass_gmail(email_addresses, email_body, 'Your Subject')
