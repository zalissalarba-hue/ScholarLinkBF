
from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))

class Bourse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200))
    pays = db.Column(db.String(100))
    description = db.Column(db.Text)

class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200))
    domaine = db.Column(db.String(100))
    description = db.Column(db.Text(200))

    class Candidature(db.Model):
        id = db.Column(db.Integer, primary_key=True)

        cv = db.Column(db.String(255))
        lettre_motivation = db.Column(db.Text)

        statut = db.Column(
            db.String(50),
            default="En attente"
        )

        utilisateur_id = db.Column(
            db.Integer,
            db.ForeignKey("user.id")
        )

        bourse_id = db.Column(
            db.Integer,
            db.ForeignKey("bourse.id"),
            nullable=True
        )

        stage_id = db.Column(
            db.Integer,
            db.ForeignKey("stage.id"),
            nullable=True
        )