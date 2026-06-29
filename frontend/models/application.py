from frontend.extensions import db

class Application(db.Model):

    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    scholarship_id = db.Column(
        db.Integer,
        db.ForeignKey("scholarships.id"),
        nullable=True
    )

    internship_id = db.Column(
        db.Integer,
        db.ForeignKey("internships.id"),
        nullable=True
    )

    statut = db.Column(
        db.String(50),
        default="En attente"
    )