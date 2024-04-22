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
Dietary Restriction(s): {order.dietary_restriction}
Delivery: {order.delivery}
Location: {order.location}
Request Time: {formatted}




From,
Pantry Pilot Team"""
    server.sendmail(sender_email, receiver_email, message)



def order_accepted_email(receiver_email,username,order):
    formatted = order.request_time.strftime("%Y-%m-%d %H:%M")
    message = f"""\
Subject: Order Accepted

Dear {username},

Your order has been acccepted by the pantry and will be fufilled!

Your order is as follows:
Order ID: {order.id}
Dietary Restriction(s): {order.dietary_restriction}
Delivery: {order.delivery}
Location: {order.location}
Request Time: {formatted}




From,
Pantry Pilot Team"""
    server.sendmail(sender_email, receiver_email, message)




def order_denied_email(receiver_email,username,order):
    formatted = order.request_time.strftime("%Y-%m-%d %H:%M")
    message = f"""\
Subject: Can't Fufill Order

Dear {username},

Pantry workers have indicated that they can not fufil your order right now and thus your order was denied.
Please try again later or create an order with differnt items.

Your order was as follows:
Order ID: {order.id}
Dietary Restriction(s): {order.dietary_restriction}
Delivery: {order.delivery}
Location: {order.location}
Request Time: {formatted}




From,
Pantry Pilot Team"""
    server.sendmail(sender_email, receiver_email, message)
    
    
    

def order_fufilled_email(receiver_email,username,order):
    formatted = order.request_time.strftime("%Y-%m-%d %H:%M")
    message = f"""\
Subject: Order Fufilled

Dear {username},

Pantry workers have indicated that your order was successfully fufilled!
We hope you enjoy your items, if there are any issues please contact us at pantrypilotuic@gmail.com

Your order was as follows:
Order ID: {order.id}
Dietary Restriction(s): {order.dietary_restriction}
Delivery: {order.delivery}
Location: {order.location}
Request Time: {formatted}




From,
Pantry Pilot Team"""
    server.sendmail(sender_email, receiver_email, message)