from flask import render_template, Blueprint, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.user import User, db
from .forms import LoginForm, RegisterForm


views = Blueprint("views", __name__)

# route for index
@views.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@views.route("/user_route", methods=["GET"])
def user_route():
    if 'user_id' in session:
        return redirect(url_for("views.user"))
    else:
        return redirect(url_for("views.login"))


@views.route("/user", methods=["GET"])
def user():
    return render_template("user.html")


@views.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():  
        existing_username = User.query.filter_by(user_name=form.user_name.data).first()
        existing_email = User.query.filter_by(email=form.email.data).first()   
        if existing_email or existing_username:
            flash("Email or username has been used", "info")
            return render_template("register.html", form = form)
        
        else:
            
            # hashed_password = generate_password_hash(form.password.data, method="sha256")
            new_user = User(name=form.name.data, user_name=form.user_name.data,
                            email=form.email.data, password=form.password.data)    
            db.session.add(new_user)
            db.session.commit()
            
            flash(f"Registration successful...please log in!: {new_user}","info")
            return redirect(url_for('views.login'))
    else:
        return render_template("register.html", form = form)
    
       

@views.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form) #retrive form info from login page
    #if the user press login and the form is filled correcly
    if request.method == "POST" and form.validate():  
        #check if the user existed in database by user_name
        existing_username = User.query.filter_by(user_name=form.user_name.data).first()  
        #if user DOES exist AND password is correct
        if existing_username and existing_username.check_password( form.password.data):
           
            # Store user information in the session (customize as needed)
            session['user_id'] = existing_username.id
            session['user_name'] = existing_username.user_name  
            session.permanent = True
            flash('Login successful!', 'success')
            return redirect(url_for('views.index')) 
        else:
            flash('Invalid username or password. Please try again.', 'error')
    
    return render_template ("login.html", form = form)
         

@views.route("/logout")
def logout():
    if "user_id" in session:
        user = session["user_name"]
        session.pop("user_name", None)
        session.pop("user_id", None)   
        flash(f"you have been logout, {user}", "info")
        return redirect(url_for("views.index"))
    
@views.route("/campuses", methods=["GET"])
def campuses():
    return render_template("campuses.html")

@views.route("/faqs", methods=["GET"])
def faqs():
    return render_template("faqs.html")