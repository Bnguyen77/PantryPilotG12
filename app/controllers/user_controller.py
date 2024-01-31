# from flask import request
# from ..models.user import User, db
# from .. import app


# @app.route("/user", methods=["POST"])
# def create_user():
#     if request.method == 'POST':
#         # Get user data from the form
#         name = request.form.get('name')
#         user_name = request.form.get('user_name')
#         email = request.form.get('email')
#         password = request.form.get('password')

#         # Create a new User instance
#         new_user = User(
#             name=name,
#             user_name=user_name,
#             email=email,
#             password=password
#         )

#         # Add the new user to the database
#         db.session.add(new_user)
#         db.session.commit()

#         return "User added successfully!"