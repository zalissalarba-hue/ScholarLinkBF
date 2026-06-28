from models import Bourse
from app import db

bourse = Bourse(
    title=titre,
    organisme=organisme,
    pays=pays,
    description=description,
    lien=lien
)

db.session.add(bourse)
db.session.commit()