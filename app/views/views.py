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
        return render_template("index.html", orders_by_user_id = orders_by_user_id)
    else:
        # This should redirect to landing page (before logged in), instead of views.login
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


@views.route('/order_request', methods=['GET'])
def order_request():
    return redirect (url_for('views.index'))
        



