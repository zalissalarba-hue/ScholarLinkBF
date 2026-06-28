from extensions import db

class Scholarship(db.Model):

    __tablename__ = "scholarships"

    id = db.Column(db.Integer, primary_key=True)

    titre = db.Column(db.String(255))

    organisme = db.Column(db.String(255))

    pays = db.Column(db.String(100))

    domaine = db.Column(db.String(100))

    niveau = db.Column(db.String(100))

    date_limite = db.Column(db.String(100))

    description = db.Column(db.Text)

    lien = db.Column(db.Text)