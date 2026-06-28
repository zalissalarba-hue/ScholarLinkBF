from flask import Flask, render_template
from config import Config
from models import db

app = Flask(__name__)

# Charger la configuration
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Initialiser SQLAlchemy
db.init_app(app)

# Créer les tables
with app.app_context():
    db.create_all()

# Route d'accueil
@app.route('/')
def accueil():
    nom_app = "ScholarLinkBF"
    return render_template('index.html', nom_app=nom_app)

@app.route('/login')
def login():
    return "<h1>Page de connexion</h1>"

@app.route('/bourses')
def bourses():
    return "<h1>Listes des bourses</h1>"

@app.route('/stages')
def stages():
    return "<h1>Liste des stages</h1>"

@app.route('/candidatures')
def candidatures():
    return "<h1>Mes candidatures</h1>"



# Lancement de l'application
if __name__ == '__main__':
    app.run(debug=True)

