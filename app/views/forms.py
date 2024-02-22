from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from ..models.user import User

class LoginForm(FlaskForm):
    user_name = StringField("User name", validators=[DataRequired()],render_kw={"placeholder": "Enter Username"})
    password = PasswordField("Password", validators=[DataRequired(),Length (8, 20)],render_kw={"placeholder": "Enter Password"})
    remember_me = BooleanField()


class RegisterForm(FlaskForm):
    user_name = StringField("Username", validators=[DataRequired()], render_kw={"placeholder": "Username"})
    name = StringField("Name", validators=[DataRequired()],render_kw={"placeholder": "Full name"})
    email = EmailField("Email", validators=[DataRequired(), Email()],render_kw={"placeholder": "someone@example.com"})
    password = PasswordField("Password", validators=[
        DataRequired() ,
        EqualTo("repassword", message="Passwords must match"),
        Length (8, 20)
        ],render_kw={"placeholder": "8-20 characters"})
    repassword = PasswordField("Confirm password", validators=[DataRequired()],render_kw={"placeholder": "8-20 characters"})
    

    