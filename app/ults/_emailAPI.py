import smtplib
import ssl



def register_email(email,name,username):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "pantrypilotuic@gmail.com"
    receiver_email = email
    password = "etsj gzqa aekn jqbu"
    message = f"""\
Subject: Welcome to Pantry Pilot!

Dear {name},


This email is to confirm you have made a Pantry Pilot account with the username {username}.
Congratulations on successfully registering, we hope you get great use out of the service!
For all inquiries, please email us at pantrypilotuic@gmail.com.




From,
Pantry Pilot Team"""


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)