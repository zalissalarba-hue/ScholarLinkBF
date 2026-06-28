import os
from werkzeug.utils import secure_filename
from flask import current_app

from models import Candidature
from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db,User,Bourse, Stage
from flask import login_manager


main = Blueprint("main", __name__)



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@main.route("/candidater/bourse/<int:id>",
            methods=["GET", "POST"])
def candidater_bourse(id):

    if request.method == "POST":

        fichier = request.files["cv"]

        nom_fichier = secure_filename(
            fichier.filename
        )

        chemin = os.path.join(
            current_app.config["UPLOAD_FOLDER"],
            nom_fichier
        )

        fichier.save(chemin)

        candidature = Candidature(
            cv=nom_fichier,
            lettre_motivation=request.form["lettre"],
            bourse_id=id
        )

        db.session.add(candidature)
        db.session.commit()

        return redirect("/dashboard")

    return render_template(
        "candidature.html"
    )



# HOME
@main.route("/")
def index():
    return render_template("index.html")


# REGISTER
@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(
            nom=request.form["nom"],
            email=request.form["email"],
            password=generate_password_hash(request.form["password"])
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("main.login"))
    return render_template("register.html")


# LOGIN
@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            session["user"] = user.id
            return redirect(url_for("main.dashboard"))
    return render_template("login.html")


# LOGOUT
@main.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.login"))


# DASHBOARD
@main.route("/dashboard")
def dashboard():
    bourses = Bourse.query.all()
    stages = Stage.query.all()
    return render_template("dashboard.html", bourses=bourses, stages=stages)


# BOURSES
@main.route("/bourses")
def bourses():
    data = Bourse.query.all()
    return render_template("bourses.html", bourses=data)


# STAGES
@main.route("/stages")
def stages():
    data = Stage.query.all()
    return render_template("stages.html", stages=data)

@main.route("/candidatures")
def candidatures():

    data = Candidature.query.all()

    return render_template(
        "candidatures.html",
        candidatures=data
    )

