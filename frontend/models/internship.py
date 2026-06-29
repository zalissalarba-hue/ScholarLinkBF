from frontend.extensions import db

class Internship(db.Model):

    __tablename__ = "internships"

    id = db.Column(db.Integer, primary_key=True)

    titre = db.Column(db.String(255))

    entreprise = db.Column(db.String(255))

    localisation = db.Column(db.String(100))

    domaine = db.Column(db.String(100))

    date_limite = db.Column(db.String(100))

    description = db.Column(db.Text)

    lien = db.Column(db.Text)