from frontend.models import Bourse
from frontend.app import db

bourse = Bourse(
    title=titre,
    organisme=organisme,
    pays=pays,
    description=description,
    lien=lien
)

db.session.add(bourse)
db.session.commit()