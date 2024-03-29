from flask import render_template, Blueprint, request, redirect, url_for, session, flash
from ..models.user import User, db
from ..models.order import Order

from ..ults._emailAPI import register_email, order_email
from datetime import datetime
from ..ults.forms import LoginForm, RegisterForm

# from app import app

order_controller = Blueprint("order_controller", __name__)

@order_controller.route('/order_request', methods=['POST'])
def order_request():
    user_id = session.get('user_id')
    # retrive data from request form
    allergies = request.form.getlist('allergies')
    dietary_restrictions = request.form.getlist('dietary_restriction')
    location = request.form.get('location')
    delivery = 0
    # Debug statements to check the value of location
    if location is not None:
        if 'uic' in location.lower():
            delivery = 0
        else:
            delivery = 1
            
    allergies_str = ', '.join(allergies) if allergies else 'none'
    dietary_restrictions_str = ', '.join(dietary_restrictions) if dietary_restrictions else 'none'
    
    new_order = Order(
        allergies = allergies_str,
        dietary_restriction=dietary_restrictions_str,
        location=location,
        delivery=delivery,
        user_id=user_id
    )

    db.session.add(new_order)
    db.session.commit()
    
    try:
        order_email(session.get('email'), session.get('user_name'), new_order)
    except Exception as e:
        # app.logger.error(f"Error sending confirmation email: {e}")
        flash("Error sending confirmation email. Please try again.", "danger")

    return redirect(url_for('views.index'))

    return redirect(url_for('views.index'))


@order_controller.route('/confirm_order/<int:order_id>', methods=['POST'])
def confirm_order(order_id):
    # Fetch the order from the database
    order = Order.query.get(order_id)
    
    if order:
        # Update the order status to "completed" and set the dispense time to now
        order.status = 'completed'
        order.dispense_time = datetime.now()
        
        # Commit changes to the database
        db.session.commit()
        
    return redirect(url_for('views.index'))

        

