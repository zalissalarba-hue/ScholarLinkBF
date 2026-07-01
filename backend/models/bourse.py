import uuid
from . import db



class Bourse(db.Model):
    __tablename__ = "bourses"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nom = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    lien = db.Column(db.String(255), nullable=False)

    # Relation many-to-many avec User
    users = db.relationship("User", secondary="users_bourses", back_populates="bourses")

    def __repr__(self):
        return f"<Bourse id={self.id} nom={self.nom} email={self.email}>"
