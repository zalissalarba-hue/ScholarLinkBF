from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Importer la table d’association en premier
from .users_bourses import UsersBourses
from .user import User
from .bourse import Bourse
