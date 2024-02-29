from .views.views import views
from .controllers.auth_controller import auth_controller
from .controllers.user_controller import user_controller
from .controllers.order_controller import order_controller
from flask import Flask
from .models import init_app, drop_database
from datetime import timedelta


# Create the Flask application
app = Flask(__name__)

# Import and initialize the models
init_app(app)
app.permanent_session_lifetime = timedelta(minutes=20)


@app.cli.command("drop_db")
def drop_db_command():
    drop_database()


# Import the views

# # Register the blueprints for views
app.register_blueprint(views)
app.register_blueprint(auth_controller)
app.register_blueprint(user_controller)
app.register_blueprint(order_controller)
