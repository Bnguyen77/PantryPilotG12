from flask import Flask
from .models import init_app, drop_database
from datetime import timedelta


# Create the Flask application
app = Flask(__name__)

# Import and initialize the models
init_app(app)
app.permanent_session_lifetime = timedelta(minutes=5)

@app.cli.command("drop_db")
def drop_db_command():
    drop_database()

# Import the views
from .views.views import views

# # Register the blueprints for views
app.register_blueprint(views)



