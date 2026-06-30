import os
from dotenv import load_dotenv

# Charger les variables depuis le fichier .env
load_dotenv()

class Config:
    # Clé secrète Flask (sessions, sécurité)
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")

    # Connexion PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        # "postgresql+psycopg2://postgres:password@localhost:5432/scholarlinkbf"
        "postgresql+psycopg2://scholarlinkbf_dev_user:scholarlinkbf_dev_password@localhost:5432/scholarlinkbf_dev_db"
    )

    # Options SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
