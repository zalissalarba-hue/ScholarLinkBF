# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import declarative_base



# Base = declarative_base()
# db = SQLAlchemy(model_class=Base)



# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     nom = Column(String, unique=False, index=True, nullable=False)
#     prenom = Column(String, unique=False, index=True, nullable=False)
#     email = Column(String, unique=True, index=True, nullable=False)
#     telephone = Column(String, unique=True, index=True, nullable=False)
#     # filiere_etude = Column(String, unique=False, index=True, nullable=True)
#     # profession = Column(String, unique=False, index=True, nullable=True)


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String, nullable=False)
    prenom = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    telephone = db.Column(db.String, unique=True, nullable=False)
    # filiere_etude = db.Column(db.String, nullable=True)
    # profession = db.Column(db.String, nullable=True)
