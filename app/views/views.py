from flask import render_template, Blueprint, request, redirect, url_for, session, flash
from ..models.user import User, db
from ..models.order import Order
from ..ults.forms import LoginForm, RegisterForm
from ..ults._emailAPI import register_email

import smtplib, ssl
# from app import app

views = Blueprint("views", __name__)

# routing for authentication

@views.route("/register", methods=["GET"])
def register():
    if 'user_id' in session:
        flash("user in session", "warning")
        return redirect(url_for("views.index"))
    else:
        form = RegisterForm(request.form)
        return render_template("register.html", form=form)


# @views.route("/login", methods=["GET", "POST"])
@views.route("/login", methods=["GET"])
def login():
    if 'user_id' in session:
        return redirect(url_for("views.index"))
    form = LoginForm(request.form)
    return render_template("login.html", form=form)


@views.route("/logout")
def logout():
    if "user_id" in session:
        user = session["user_name"]
        session.pop("user_name", None)
        session.pop("user_id", None)
        flash(f"You have been logged out, {user}", "info")
        return redirect(url_for("views.index"))
    return redirect(url_for('views.login'))


# ROUTING FOR INDEX
@views.route("/", methods=["GET"])
def index():
    if 'user_id' in session:
        user_id = session.get('user_id')
        orders_by_user_id = Order.query.filter_by(user_id=user_id).all()
        return render_template("index.html", orders_by_user_id=orders_by_user_id)
    else:
        return redirect(url_for("views.login"))

# ROUTING FOR USER


@views.route("/user_route", methods=["GET"])
def user_route():
    if 'user_id' in session:
        return redirect(url_for("views.user"))
    else:
        return redirect(url_for("views.login"))


@views.route("/user", methods=["GET"])
def user():
    if 'user_id' in session:
        # Retrieve user_id from session
        user_id = session.get('user_id')
        # Query the database to get the user information
        user = User.query.get(user_id)
        # Pass user information to the template
        return render_template("user.html", user=user)
    else:
        flash("login to access this page", "warning")
        return redirect(url_for("views.index"))


@views.route("/user_edit", methods=["POST"])
def user_edit():
    if 'user_id' in session:
        user_id = session.get('user_id')

        new_bio = request.form.get('bio')

        user = User.query.get(user_id)
        user.bio = new_bio

        db.session.commit()
        return redirect(url_for("views.user"))
    else:
        return redirect(url_for("views.user"))


@views.route("/campuses", methods=["GET"])
def campuses():
    return render_template("campuses.html")


@views.route("/faqs", methods=["GET"])
def faqs():
    return render_template("faqs.html")


@views.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@views.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")


@views.route('/order_request', methods=['GET', 'POST'])
def order_request():
    if request.method == 'POST':
        user_id = session.get('user_id')
        # retrive data from request form
        prefer_item = request.form.get('prefer_item')
        dietary_restriction = request.form.get('dietary_restriction')
        location = request.form.get('location')
        delivery = 0
        # Debug statements to check the value of location
        if location is not None:
            if 'uic' in location.lower():
                delivery = 0
            else:
                delivery = 1

        # After processing the form data, you can redirect to another page

        new_order = Order(
            prefer_item=prefer_item,
            dietary_restriction=dietary_restriction,
            location=location,
            delivery=delivery,
            user_id=user_id
        )

        db.session.add(new_order)
        db.session.commit()

        return redirect(url_for('views.index'))
    else:
        # Render the order request form template
        return render_template('order_request_form.html')


@views.route('/submit_order_success')
def submit_order_success():
    # Render a success page after submitting the order
    return render_template('submit_order_success.html')


# def register_email(email,name,username):
#     port = 465  # For SSL
#     smtp_server = "smtp.gmail.com"
#     sender_email = "pantrypilotuic@gmail.com"
#     receiver_email = email
#     password = "etsj gzqa aekn jqbu"
#     message = f"""\
# Subject: Welcome to Pantry Pilot!

# Dear {name},


# This email is to confirm you have made a Pantry Pilot account with the username {username}.
# Congratulations on successfully registering, we hope you get great use out of the service!
# For all inquiries, please email us at pantrypilotuic@gmail.com.




# From,
# Pantry Pilot Team"""


#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message)