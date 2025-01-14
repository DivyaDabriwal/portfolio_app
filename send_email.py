import smtplib, ssl, os

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    receiver_email = os.getenv("EMAIL")
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver_email, msg=message)
        return 'Sent'
    except Exception as e:
        print('Exception Occurred: ', e)
        return 'Error'