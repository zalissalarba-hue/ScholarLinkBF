from marshmallow import validates, ValidationError
from flask_marshmallow import Marshmallow
from models.user import User

ma = Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True   # Retourne directement une instance User

  #  @validates("email")
   # def validate_email(self, value):
        # Vérifie si l'email existe déjà
     #   if User.query.filter_by(email=value).first():
       #     raise ValidationError("Email already exists")
       