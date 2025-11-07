from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Route principale pour afficher la page
@app.route('/')
def index():
    return render_template('index.html')

# Nouvelle route API pour fournir l'heure du serveur
@app.route('/time_update')
def time_update():
    # Récupère l'heure actuelle du serveur
    now = datetime.now()
    
    # Formate l'heure comme une chaîne de caractères (ex: 14:06:47)
    current_time = now.strftime("%H:%M:%S")
    
    # Retourne l'heure formatée en tant que JSON
    # C'est la réponse que le JavaScript recevra.
    return jsonify(time=current_time)

if __name__ == '__main__':
    # Le mode debug permet de redémarrer automatiquement le serveur
    app.run(debug=True)
