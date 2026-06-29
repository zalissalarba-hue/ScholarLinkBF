from flask import Flask
from flask_restful import Api
from resources import UserResource
from models import User, db
from schemas import ma



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///scholarlinkbf.db"



db.init_app(app)
ma.init_app(app)


api = Api(app)
api.add_resource(UserResource, "/users", "/users/<int:user_id>")

with app.app_context() :
    try:
        db.drop_all()
        db.create_all()

        rodrigue = User(nom="SON", prenom="Rodrigue", email="sonrodrigue@gmail.com", telephone="0022645123276")
        robert = User(nom="KOUDA", prenom="Robert", email="koudarobert@gmail.com", telephone="0022646123276")

        db.session.add(rodrigue)
        db.session.add(robert)
        db.session.commit()

        rodrigue_db = db.session.query(User).filter(User.nom == "SON").first()
        robert_db = db.session.query(User).filter(User.nom == "KOUDA").first()

        print(f"{rodrigue_db.id}: {rodrigue_db.nom}  - {rodrigue_db.prenom}")
        print(f"{robert_db.id}: {robert_db.nom}  - {robert_db.prenom}")
        app.run()
    except Exception as ex :
        print(ex)

# @app.route("/")
# def home():
#     return "<h1>Bienvenue sur ScholarLinkBF!</h1>"


# if __name__ == "__main__" :
#     app.run(debug=True, host="127.0.0.1", port=5000)