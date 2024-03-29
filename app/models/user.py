from flask_avatars import Identicon  # Import Identicon style from Flask Avatars
from flask import current_app
from . import db
import os
import string
from ..ults.randomString import random_string


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    bio = db.Column(db.Text)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    avatar = db.relationship('Avatar', backref='user', uselist=False)

    def check_password(self, password):
        return password == self.password

    def generate_avatar(self):
        # Generate a random Identicon avatar URL
        avatar = Identicon()
        # Assuming you have a configuration variable for the save path
        path = current_app.config['AVATARS_SAVE_PATH']
        # Delete previous avatar files if they exist
        if self.avatar:
            previous_avatar_paths = [
                os.path.join(path, getattr(self.avatar, f'avatar_url_{size}'))
                for size in ['s', 'm', 'l']
            ]
            for previous_avatar_path in previous_avatar_paths:
                if os.path.exists(previous_avatar_path):
                    os.remove(previous_avatar_path)
        # Generate new avatar URLs for all three sizes
        fileNames = avatar.generate(text=random_string(5, self.user_name))
        # Assuming fileNames contains URLs for small, medium, and large avatars
        avatar_urls = fileNames[:3]
        # Create or update the avatar associated with the user
        if self.avatar:
            self.avatar.avatar_url_s, self.avatar.avatar_url_m, self.avatar.avatar_url_l = avatar_urls
        else:
            self.avatar = Avatar(
                user_id=self.id,
                avatar_url_s=avatar_urls[0],
                avatar_url_m=avatar_urls[1],
                avatar_url_l=avatar_urls[2]
            )
        db.session.commit()


class Avatar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), unique=True, nullable=False)
    avatar_url_s = db.Column(db.String(255), nullable=False)
    avatar_url_m = db.Column(db.String(255), nullable=False)
    avatar_url_l = db.Column(db.String(255), nullable=False)


