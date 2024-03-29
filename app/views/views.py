from flask import render_template, Blueprint, request, redirect, url_for, session, flash
from ..models.user import User, Avatar, db
from ..models.order import Order
from ..ults.forms import LoginForm, RegisterForm
from sqlalchemy import desc, and_  # Import the desc method


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
        session.pop("user_id", None)
        session.pop("user_name", None)
        session.pop("email", None)
        session.pop("name", None)
        session.pop("role", None)
        flash(f"You have been logged out, {user}", "info")
        return redirect(url_for("views.index"))
    return redirect(url_for('views.login'))

# ROUTING FOR INDEX


@views.route("/", methods=["GET"])
def index():
    if 'user_id' in session:
        is_admin = session.get('role')
        if is_admin == 1:
            return redirect(url_for("views.admin"))
        user_id = session.get('user_id')
        user = User.query.get(user_id)
        orders_by_user_id = Order.query.filter_by(
            user_id=user_id).order_by(desc(Order.request_time)).all()
        return render_template("index.html", user = user,orders_by_user_id=orders_by_user_id)
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
    return redirect(url_for('views.index'))


@views.route('/admin', methods=['GET'])
def admin():
    if 'user_id' in session:
        is_admin = session.get('role')
        if is_admin == 1:
            user = User.query.get(session['user_id'])
            pending_delivery_orders = Order.query.filter(and_(
                Order.status == 'pending', Order.delivery == True)).order_by(Order.request_time).all()

            pending_pickup_orders = Order.query.filter(and_(
                Order.status == 'pending', Order.delivery == False)).order_by(Order.request_time).all()

            completed_orders = Order.query.filter(
                Order.status != 'pending').all()
            # Fetch avatar URLs for users associated with orders
            for order in pending_delivery_orders + pending_pickup_orders + completed_orders:
                order.user_avatar_url = order.user.avatar if order.user else None

            return render_template("admin.html", user=user, PDO=pending_delivery_orders, PPO=pending_pickup_orders, CO=completed_orders)

    flash("unauthorized access", "danger")
    return redirect(url_for("views.index"))
