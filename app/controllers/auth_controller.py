from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from ..models.user import User, db
from ..views.forms import LoginForm, RegisterForm

auth_controller = Blueprint("auth_controller", __name__)
