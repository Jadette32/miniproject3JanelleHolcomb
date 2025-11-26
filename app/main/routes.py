# INF601 - Advanced Programming in Python
# Janelle Holcomb
# Final Project


"""
File: app/main/routes.py
Description: Main blueprint routes (home, about, dashboard, notes)
"""

from ..helpers import create_mood_chart
from flask import current_app
from ..helpers import get_quote_for_mood
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from .. import db
from ..models import Note
from ..forms import NoteForm

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/about")
def about():
    return render_template("about.html")



@main_bp.route("/dashboard")
@login_required
def dashboard():
    note_count = Note.query.filter_by(user_id=current_user.id).count()

    latest_note = Note.query.filter_by(user_id=current_user.id).order_by(Note.created_at.desc()).first()

    if latest_note:
        quote = get_quote_for_mood(latest_note.mood)
    else:
        quote = get_quote_for_mood("calm")

    # create the mood chart
    chart_filename = create_mood_chart(current_app)

    return render_template(
        "dashboard.html",
        note_count=note_count,
        quote=quote,
        chart_filename=chart_filename
    )


@main_bp.route("/notes")
@login_required
def notes():
    items = Note.query.filter_by(user_id=current_user.id).order_by(Note.created_at.desc()).all()
    return render_template("notes.html", items=items)


@main_bp.route("/notes/add", methods=["GET", "POST"])
@login_required
def add_note():
    form = NoteForm()
    if form.validate_on_submit():
        n = Note(
            title=form.title.data,
            body=form.body.data,
            mood=form.mood.data,         # <-- ADDED MOOD HERE
            user_id=current_user.id
        )
        db.session.add(n)
        db.session.commit()
        flash("Note added.", "success")
        return redirect(url_for("main.notes"))
    return render_template("add_note.html", form=form)
