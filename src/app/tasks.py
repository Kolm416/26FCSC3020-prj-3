'''
CSC3020 - Software Engineering Fundamentals
Instructor: Thyago Mota
Student(s): Juvia Archuleta, Leigha Lennon
Description: Project 3 - TaskTrack
'''

from flask import Blueprint, render_template
from flask_login import login_required

tasks = Blueprint("tasks", __name__)
@tasks.get("/tasks")
@login_required
def dashboard():
    
    # US5: Load the signed-in user's saved tasks in Sprint 3.
    return render_template("tasks.html")