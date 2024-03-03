import smtplib
import ssl
from datetime import datetime

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "pantrypilotuic@gmail.com"
password = "etsj gzqa aekn jqbu"
context = ssl.create_default_context()
server=smtplib.SMTP_SSL(smtp_server, port, context=context)
server.login(sender_email, password)

def register_email(receiver_email,name,username):
    message = f"""\
Subject: Welcome to Pantry Pilot!

Dear {name},


This email is to confirm you have made a Pantry Pilot account with the username {username}.
Congratulations on successfully registering, we hope you get great use out of the service!
For all inquiries, please email us at pantrypilotuic@gmail.com.




From,
Pantry Pilot Team"""
    server.sendmail(sender_email, receiver_email, message)


def order_email(receiver_email,username,order):
    formatted = order.request_time.strftime("%Y-%m-%d %H:%M")
    message = f"""\
Subject: Order Confirmation

Dear {username},

This email is to confirm you have successfully placed an order with Pantry Pilot.

Your order is as follows:
Order ID: {order.id}
Preferred Item(s): {order.prefer_item}
Dietary Restriction(s): {order.dietary_restriction}
Delivery: {order.delivery}
Location: {order.location}
Request Time: {formatted}




From,
Pantry Pilot Team"""
    server.sendmail(sender_email, receiver_email, message)