'''
CSC3020 - Software Engineering Fundamentals
Instructor: Thyago Mota
Student(s): Juvia Archuleta, Leigha Lennon
Description: Project 3 - TaskTrack
'''

import os
import secrets

from flask import Flask, redirect, render_template, url_for
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

from .auth import auth
from .models import db, User
from .tasks import tasks

def create_app():
    app = Flask(__package__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY") or secrets.token_hex(32)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasktrack.db"

    db.init_app(app)
    CSRFProtect(app)

    # US2: Send signed out visitors to login when they open /tasks.
    login_manager = LoginManager(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    @app.get("/")
    def index():
        return redirect(url_for("auth.login"))

    # Connect the routes defined in auth.py and tasks.py.
    app.register_blueprint(auth)
    app.register_blueprint(tasks)

    with app.app_context():
        db.create_all()

    return app