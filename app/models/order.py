from . import db
from datetime import datetime

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    allergies = db.Column(db.String(200), nullable=False, default='none')
    dietary_restriction = db.Column(db.String(200), nullable=False, default='none')
    status = db.Column(db.String(20), nullable=False, default='pending')
    delivery = db.Column(db.Boolean, nullable=False, default=False)  # True if delivery, False if pickup
    location = db.Column(db.String(200),nullable=False, default='UIC')  # Location for delivery orders
    request_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    dispense_time = db.Column(db.DateTime,nullable=True)  # Dispense time for completed orders

    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    
    
    @classmethod
    def get_order_count(cls):
        return cls.query.count()