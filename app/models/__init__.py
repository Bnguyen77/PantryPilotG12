from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import csv
from flask_avatars import Avatars
# Create SQLAlchemy instances
db = SQLAlchemy()


def init_app(app):
    # Configure the Flask app
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
    # Ensure that templates are auto-reloaded during development
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    
    from .user import User
    from .order import Order
    # Initialize the SQLAlchemy database
    db.init_app(app)
    avatars = Avatars(app)
    # Create the database tables
    with app.app_context():
        db.create_all()
        
    


    
    
# def process_csv(filename):
#     from .order import Order
#     with open(filename, 'r', newline='') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             pickup_time = datetime.strptime(
#                 row['pickup_time'], '%Y-%m-%d %H:%M:%S') if row['pickup_time'] else None
#             # Create an Order object and save it to the database
#             order = Order(
#                 user_id=int(row['user_id']),
#                 pickup_time=pickup_time,
#                 items=row['items'],
#                 status=row['status'],
#                 donor=row['donor']
#             )
#             db.session.add(order)
#         # Commit the changes to the database
#         db.session.commit()



