from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importer ton modèle User pour que SQLAlchemy le connaisse
from .user import User
