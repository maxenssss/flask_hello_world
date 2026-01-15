import os
import time
from flask import Flask
from pyngrok import ngrok

app = Flask(__name__)

@app.route('/')
def home():
    return "Serveur en Preview - Contenu du Repo GitHub"

if __name__ == '__main__':
    # Configuration du token depuis la variable d'environnement
    NGROK_TOKEN = os.environ.get("NGROK_AUTHTOKEN")
    ngrok.set_auth_token(NGROK_TOKEN)

    # Création du tunnel
    public_url = ngrok.connect(5000).public_url
    print(f" * URL Publique : {public_url}")

    # Écriture de l'URL dans un fichier pour l'artefact GitHub
    with open("url_preview.txt", "w") as f:
        f.write(public_url)

    # Lancement de Flask et arrêt automatique après 300s
    # Note : GitHub Actions tuera le process à la fin du temps imparti
    app.run(port=5000)
