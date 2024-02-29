from flask import render_template, Blueprint, request, redirect, url_for, session, flash
from ..models.user import User, db
from ..models.order import Order
from ..ults.forms import LoginForm, RegisterForm
from ..ults._emailAPI import register_email


user_controller = Blueprint("user_controller", __name__)


@user_controller.route("/user_edit", methods=["POST"])
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