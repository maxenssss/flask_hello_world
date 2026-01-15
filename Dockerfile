FROM python:3.9-slim

# Installation de curl pour télécharger ngrok
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Installation de Flask et pyngrok
RUN pip install flask pyngrok

# Copie des fichiers du repo dans l'image
WORKDIR /app
COPY . .

# On expose le port 5000 (port par défaut de Flask)
EXPOSE 5000

# Lancement du script de démarrage
CMD ["python", "app.py"]
