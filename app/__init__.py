# INF601 - Advanced Programming in Python
# Janelle Holcomb
# Final Project


"""
File: app/__init__.py
Description: App factory, DB and Login setup
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import click

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Use instance folder for SQLite file
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(app.instance_path, "app.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    db.init_app(app)
    login_manager.init_app(app)

    from .models import User, Note

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth.routes import auth_bp
    from .main.routes import main_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")

    app.register_blueprint(main_bp)

    # 🌿 Add the init-db command (professor REQUIRED this)
    @app.cli.command("init-db")
    def init_db():
        """Initialize the database."""
        click.echo("Dropping existing tables...")
        db.drop_all()
        click.echo("Creating new tables...")
        db.create_all()
        click.echo("Database initialized successfully.")

    return app

