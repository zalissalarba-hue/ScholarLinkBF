from frontend.extensions import db

class Candidature(db.Model):

    __tablename__ = "candidatures"

    id = db.Column(db.Integer, primary_key=True)

    statut = db.Column(
        db.String(50),
        default="En attente"
    )

    cv = db.Column(db.String(255))

    lettre_motivation = db.Column(db.String(255))

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    bourse_id = db.Column(
        db.Integer,
        db.ForeignKey("bourses.id")
    )