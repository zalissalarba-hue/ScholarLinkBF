
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from frontend.config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "main.login"

    from frontend.views.ROUTES import main
    app.register_blueprint(main)

    with app.app_context():
        from flask import models
        db.create_all()

    return app