from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))

class Bourse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200))
    pays = db.Column(db.String(100))
    description = db.Column(db.Text)
    niveau = db.Column(db.String(100))
    date_debut = db.Column(db.String(50))
    date_limite = db.Column(db.String(50))
    

class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200))
    domaine = db.Column(db.String(100))
    description = db.Column(db.Text)