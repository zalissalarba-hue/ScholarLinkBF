from schemas import ma
from models import Bourse

class BourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Bourse
        load_instance = True
