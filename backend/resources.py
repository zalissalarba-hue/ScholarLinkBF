

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from models import User
from schemas import UserSchema
from models import db


class UserResource(Resource):

    user_schema = UserSchema()
    user_list_schema = UserSchema(many=True)

    def get(self, user_id=None):
        if user_id :
            user = User.query.get_or_404(user_id)
            return self.user_schema.dump(user)
        else :
            all_users = User.query.all()
            return self.user_list_schema.dump(all_users)
    
    # def post(self):
    #     try:
    #         new_user_data = self.user_schema.load(request.json)
    #         # new_user = User(**user_data)
    #         # db.session.add(new_user)
    #         # db.session.commit()
    #         # return self.user_schema.dump(new_user), 201
    #     except ValidationError as err:
    #         return {"message": "Validation error: ", "errors": err.messages}, 400

    #     # new_user = User(**new_user_data)
    #     new_user = User(
    #         nom=new_user_data["nom"],
    #         prenom=new_user_data["prenom"],
    #         email=new_user_data["email"],
    #         telephone=new_user_data["telephone"]
    #     )
    #     db.session.add(new_user)
    #     db.session.commit()
    #     return self.user_schema.dump(new_user)

    def post(self):
        try:
            new_user = self.user_schema.load(request.json)  # retourne directement une instance User si load_instance=True
        except ValidationError as err:
            return {"message": "Validation error", "errors": err.messages}, 400

        db.session.add(new_user)
        db.session.commit()
        return self.user_schema.dump(new_user), 201

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        try:
            updated_user = self.user_schema.load(request.json, instance=user, partial=True)
            db.session.commit()
            return self.user_schema.dump(updated_user)
        except ValidationError as err:
            return {"message": "Validation error", "errors": err.messages}, 400

        for key, value in updated_user_data.items():
            setattr(user, key, value)

        db.session.commit()
        return self.user_schema.dump(user)
    
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully."}, 200
