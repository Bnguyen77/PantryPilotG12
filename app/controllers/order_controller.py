from flask import render_template, Blueprint, request, redirect, url_for, session, flash
from ..models.user import User, db
from ..models.order import Order
from ..ults._emailAPI import register_email
# from app import app

order_controller = Blueprint("order_controller", __name__)

@order_controller.route('/order_request', methods=['POST'])
def order_request():
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