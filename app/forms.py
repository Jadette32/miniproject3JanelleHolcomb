# INF601 - Advanced Programming in Python
# Janelle Holcomb
# Final Project - Mindful Moments

"""
File: app/forms.py
Description: WTForms for authentication and notes
"""

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    TextAreaField,
    SubmitField,
    SelectField
)
from wtforms.fields import DateField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Create Account")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")


class NoteForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=120)])
    body = TextAreaField("Body", validators=[DataRequired()])
    mood = SelectField("Mood", choices=[("happy","Happy"),("sad","Sad"),("anxious","Anxious"),("tired","Tired"),("calm","Calm")])
    reflection_date = DateField("Reflection Date", validators=[DataRequired()])
    submit = SubmitField("Save")
