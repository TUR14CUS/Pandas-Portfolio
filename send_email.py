import ssl, smtplib
import os
import ssl
import smtplib
import os
import logging


def send_email(message):
    host = ''  # your email host
    port = ''  # your email port

    username = os.getenv("EMAIL")  # your email address
    password = os.getenv("PASSWORD")  # your email password

    receivers = ['']  # list of receiver email addresses
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receivers, message)
            logging.info("Email sent successfully")
    except smtplib.SMTPException as e:
        logging.error(f"Failed to send email: {str(e)}")

