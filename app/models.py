# INF601 - Advanced Programming in Python
# Janelle Holcomb
# Final Project

"""
File: app/models.py
Description: SQLAlchemy models (User ↔ Note)
"""

from datetime import datetime
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    notes = db.relationship("Note", backref="author", lazy=True)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    mood = db.Column(db.String(20), nullable=False)     # ← FIXED: inside class
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
