'''
CSC3020 - Software Engineering Fundamentals
Instructor: Thyago Mota
Student(s): Juvia Archuleta, Leigha Lennon
Description: Project 3 - TaskTrack
'''

"""
CSC3020 - Software Engineering Fundamentals
Instructor: Thyago Mota
Student(s): Juvia Archuleta, Leigha Lennon
Description: Sprint 2 registration, login, and logout routes.
"""

from flask import (Blueprint, flash, redirect, render_template, request, session, url_for)
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy.exc import IntegrityError

from .models import User, db

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    #US1: Create an account and direct the new user to the login page
    if current_user.is_authenticated:
        return redirect(url_for("tasks.dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or len(username) > 80 or not password.strip():
            flash("Enter a username of up to 80 characters and a password.")
        else:
            user = User(username=username)
            user.set_password(password)
            db.session.add(user)

            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                flash("That username is already taken.")
            else:
                flash("Account created. You can now log in.")
                return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    #US2: Sign in with valid credentials and open the user's task page.
    if current_user.is_authenticated:
        return redirect(url_for("tasks.dashboard"))

    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")
    user = db.session.execute(db.select(User).filter_by(username=username)).scalar_one_or_none()

    if user is None or not user.check_password(password):
        flash("Invalid username or password.")
        return render_template("login.html")   
    session.clear()
    login_user(user)
    return redirect(url_for("tasks.dashboard"))


@auth.post("/logout")
@login_required
def logout():
    #US3: End the user's session and return them to the login page.
    logout_user()
    session.clear()
    flash("You have logged out.")
    return redirect(url_for("auth.login"))