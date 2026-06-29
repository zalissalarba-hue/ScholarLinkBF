from flask import Blueprint

stages_bp = Blueprint('stages', __name__)

@stages_bp.route('/stages')
def liste_stages():
    return "Liste des stages"