# from flask_marshmallow import Marshmallow

# from models import User

# ma = Marshmallow()

# class UserSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = User


from flask_marshmallow import Marshmallow
from models import User

ma = Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True   # permet de charger directement en instance SQLAlchemy
