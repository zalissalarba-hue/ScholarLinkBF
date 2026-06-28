from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from extensions import db
from models.user import User

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    user = User(
        nom=data["nom"],
        email=data["email"],
        password=generate_password_hash(
            data["password"]
        ),
        domaine=data["domaine"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "Compte créé"
    })