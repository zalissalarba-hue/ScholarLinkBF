from frontend.extensions import db

class Bourse(db.Model):

    __tablename__ = "bourses"


Id = db.Column(db.Integer, primary_key=True)
Titre = db.Column(db.String(200))
Niveau = db.Column(db.String(100))
pays = db.Column(db.String(100))
Montant = db.Column(db.Float)
Description = db.Column(db.Text)
Structure_id = db.Column(
        db.Integer,
        db.ForeignKey("structures.id")
    )