from flask import render_template, Blueprint, request, redirect, url_for, session, flash, jsonify
from ..models.user import User, db
from ..models.order import Order
from ..ults._emailAPI import register_email, order_email, order_accepted_email, order_denied_email
from datetime import datetime



# from app import app

order_controller = Blueprint("order_controller", __name__)

@order_controller.route('/order_request', methods=['POST'])
def order_request():
    user_id = session.get('user_id')
    # retrive data from request form
    allergies = request.form.getlist('allergies')
    dietary_restrictions = request.form.getlist('dietary_restriction')
    delivery_str = request.form.get('delivery')
    
    if delivery_str == '0':
        delivery = False
    else:
        delivery = True
    # Debug statements to check the value of location   
    if delivery == 0:
        location = "UIC"
    else:
        location = request.form.get('location')
            
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

    
@order_controller.route('/confirm_order/<int:order_id>', methods=['POST'])
def confirm_order(order_id):
    # Fetch the order from the database
    order = Order.query.get(order_id)
    if order:
        # Update the order status to "completed" and set the dispense time to now
        order.status = 'confirmed'
        order.dispense_time = datetime.now()
        db.session.commit()
        order_user = User.query.get(order.user_id)
        try:
            order_accepted_email(order_user.email, order_user.user_name, order)
            flash('order confirmed email', 'success')  
        except Exception as e:
            flash("Error sending acceptance email. Please try again.", "danger")   
            
    return redirect(url_for('views.index'))


@order_controller.route('/deny_order/<int:order_id>', methods=['POST'])
def deny_order(order_id):
    # Fetch the order from the database
    order = Order.query.get(order_id)
    
    if order:
        db.session.delete(order)
        db.session.commit()
        try:
            order_user = User.query.get(order.user_id)
            order_denied_email(order_user.email, order_user.user_name, order)
            flash('order denied email', 'success')  
        except Exception as e:
            flash("Error sending acceptance email. Please try again.", "danger")   
    return redirect(url_for('views.index'))


@order_controller.route('/fulfill_order/<int:order_id>', methods=['POST'])
def fulfill_order(order_id):
    # Fetch the order from the database
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        try:
            user = User.query.get(session.get('user_id'))
            order_accepted_email(user.email, user.user_name, order)
            flash('order denied email', 'success')  
        except Exception as e:
            flash("Error sending acceptance email. Please try again.", "danger")   
    return redirect(url_for('views.index'))


@order_controller.route('/order_edit', methods=['POST'])
def order_edit():
        data = request.json  # Retrieve JSON data from the request
        order_id = data.get('order_id')
        allergies = data.get('allergies')
        dietary_restrictions = data.get('dietary_restrictions')

        # Fetch the order from the database
        order = Order.query.get(order_id)
        
        if order:
            # Update the order with the edited data
            order.allergies = ', '.join(allergies)
            order.dietary_restriction = ', '.join(dietary_restrictions)
            order.allergies = ', '.join(allergies) if allergies else 'None'
            order.dietary_restriction = ', '.join(dietary_restrictions) if dietary_restrictions else 'None'

            db.session.commit()
            flash('Order updated successfully', 'success')
        else:
            flash(f'Order not found - {order_id}', 'error')

        return jsonify({'success': True})
    



@order_controller.route('/order_delete', methods=['POST'])
def order_delete():
    # Retrieve the order ID from the JSON data sent in the request
    order_id = request.json.get('order_id')

    # Fetch the order from the database
    order = Order.query.get(order_id)
    
    if order:
        # Delete the order from the database
        db.session.delete(order)
        db.session.commit()
        flash('Order deleted successfully', 'success')
    else:
        flash('Order not found', 'error')
    
    # Redirect to the index page or any other appropriate page
    return jsonify({'success': True})

        

