from flask import render_template, Blueprint, request, redirect, url_for, session, flash
from ..models.user import User, db
from ..models.order import Order
from ..ults.forms import LoginForm, RegisterForm
from ..ults._emailAPI import register_email


# from app import app

auth_controller = Blueprint("auth_controller", __name__)


@auth_controller.route("/register", methods=["POST"])
def Register():
    form = RegisterForm(request.form)
    if form.validate():
        existing_username = User.query.filter_by(
            user_name=form.user_name.data).first()
        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_email or existing_username:
            flash("Email or Username has been used", "info")
            return render_template("register.html", form=form)
        else:
            # hashed_password = generate_password_hash(form.password.data, method="sha256")
            is_volunteer = bool(int(request.form.get('is_volunteer', 0)))             
            new_user = User(name=form.name.data, user_name=form.user_name.data,
                            email=form.email.data, password=form.password.data, is_admin = is_volunteer)
            db.session.add(new_user)
            db.session.commit()

            try:
                register_email(new_user.email, new_user.name,
                               new_user.user_name)
            except Exception as e:
                # app.logger.error(f"Error sending confirmation email: {e}")
                flash("Error sending registration email. Please try again.", "danger")

            flash(
                f"Registration successful...please log in!: {new_user.user_name}", "success")
            return redirect(url_for('views.login'))


@auth_controller.route("/login", methods=["POST"])
def Login():
    form = LoginForm(request.form)  # retrive form info from login page
    # if the user press login and the form is filled correcly
    if form.validate():
        # check if the user existed in database by user_name
        existing_username = User.query.filter_by(
            user_name=form.user_name.data).first()
        # if user DOES exist AND password is correct
        if existing_username and existing_username.check_password(form.password.data):

            # Store user information in the session (customize as needed)
            session['user_id'] = existing_username.id
            session['user_name'] = existing_username.user_name
            session['email'] = existing_username.email
            session['name'] = existing_username.name
            session['role'] = existing_username.is_admin

            session.permanent = True
            flash('Login successful!', 'success')
            return redirect(url_for('views.index'))

        else:
            flash('Invalid username or password. Please try again.', 'error')
            return redirect(url_for('views.login'))


@auth_controller.route('/generate_avatar/<int:user_id>')
def generate_avatar(user_id):
    if 'user_id' in session and user_id == session.get('user_id'):
        user = User.query.get(user_id)  
        if user:
            user.generate_avatar()
    return redirect(url_for('views.user'))
