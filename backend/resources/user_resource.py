from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from models.user import User, db
from schemas.user_schema import UserSchema

class UserResource(Resource):
    user_schema = UserSchema()
    user_list_schema = UserSchema(many=True)

    def get(self, user_id=None):
        if user_id:
            user = User.query.get_or_404(user_id)
            return self.user_schema.dump(user)
        else:
            all_users = User.query.all()
            return self.user_list_schema.dump(all_users)

    def post(self):
        try:
            new_user = self.user_schema.load(request.json)
        except ValidationError as err:
            return {"message": "Validation error", "errors": err.messages}, 400

        db.session.add(new_user)
        db.session.commit()
        return self.user_schema.dump(new_user), 201

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        try:
            updated_user = self.user_schema.load(request.json, instance=user, partial=True)
        except ValidationError as err:
            return {"message": "Validation error", "errors": err.messages}, 400

        db.session.commit()
        return self.user_schema.dump(updated_user)

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully"}, 200
