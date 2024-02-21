from . import db
from datetime import datetime

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default = 999)  # Nullable user_id
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    pickup_time = db.Column(db.DateTime, nullable=True, default=None)  # Nullable pickup_time
    items = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=True, default=None)
    donor = db.Column(db.String(20), nullable=True, default=None)
    
    @classmethod
    def get_order_count(cls):
        return cls.query.count()