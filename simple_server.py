from flask import Flask

# Crée une instance de l'application Flask
app = Flask(__name__)

# Définit l'itinéraire pour la page d'accueil (/)
@app.route('/')
def hello_world():
    # Renvoie la chaîne à afficher sur la page web
    return 'Hello World!'

# Exécute l'application si le script est lancé directement
if __name__ == '__main__':
    app.run(debug=True)
