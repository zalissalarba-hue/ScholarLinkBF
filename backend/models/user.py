import uuid
from . import db



class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    # Relation many-to-many avec Bourse
    bourses = db.relationship("Bourse", secondary="users_bourses", back_populates="users")

    def __repr__(self):
        return f"<User id={self.id} email={self.email} nom={self.nom} prenom={self.prenom}>"
