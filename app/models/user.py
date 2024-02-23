from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    bio = db.Column(db.Text)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def check_password(self, password):
        return password == self.password


# setting api call for user
