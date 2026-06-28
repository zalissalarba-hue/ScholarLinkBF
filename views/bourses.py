from flask import Blueprint

bourses_bp = Blueprint("bourses", __name__)

@bourses_bp.route("/bourses")
def liste_bourses():
    return "Liste des bourses"