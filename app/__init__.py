from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, request, redirect, url_for, flash, session


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)

    # ✅ Correct imports
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp

    # ✅ Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app
