from .views.views import views
from .controllers.auth_controller import auth_controller
from .controllers.user_controller import user_controller
from .controllers.order_controller import order_controller
from flask import Flask
import os

from .models import init_app
from datetime import timedelta


# Create the Flask application
app = Flask(__name__)


# Import and initialize the models
init_app(app)

app.permanent_session_lifetime = timedelta(minutes=20)


# Import the views

# # Register the blueprints for views
app.register_blueprint(views)
app.register_blueprint(auth_controller)
app.register_blueprint(user_controller)
app.register_blueprint(order_controller)



# Get the absolute path to the directory containing this script
basedir = os.path.abspath(os.path.dirname(__file__))
# Set the AVATARS_SAVE_PATH configuration variable to the "avatars" directory
avatars_dir = os.path.join(basedir, 'static/avatars')
if not os.path.exists(avatars_dir):
    os.makedirs(avatars_dir)
app.config['AVATARS_SAVE_PATH'] = avatars_dir