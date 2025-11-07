from flask import Flask

# Crée une instance de l'application Flask
app = Flask(__name__)

# --- MODIFICATION CLÉ ---
# Définit une route qui accepte une variable 'name'
# La variable est entre < > et son type par défaut est string
@app.route('/hello/<name>')
def hello_name(name):
    # La fonction reçoit la valeur de l'URL comme argument 'name'
    # Elle renvoie la chaîne formatée
    return f'Hello World! Mon nom est {name}!'

# Route par défaut (si aucun nom n'est fourni)
@app.route('/')
def hello_default():
    return 'Hello World!'

# Exécute l'application
if __name__ == '__main__':
    app.run(debug=True)
