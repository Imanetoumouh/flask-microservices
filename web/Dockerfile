# Dockerfile pour l'application web
# Ce Dockerfile sera basé sur l'image officielle de Python Docker

FROM python
# Installez les dépendances de l'application web
RUN apt-get update && apt-get install -y python3-pip

COPY requirements.txt .

# Pour définir la variable d'environnement DATABASE_HOST
# variable d'environnement est utilisée par l'application Flask pour se connecter à la base de données MySQL.
ENV DATABASE_HOST db

# Installez les dépendances de l'application web
RUN pip install -r requirements.txt

RUN pip install flask flask-sqlalchemy mysql-connector-python


# The MySQL client allows you to connect to the MySQL server and run SQL commands
RUN apt-get update && apt-get install -y mysql-client

# Copiez l'application web dans le conteneur
COPY app.py .
COPY registration.html .
COPY index.html .
COPY registration.txt .


# Définissez le point de montage pour les données de l'application web
VOLUME /app/data

# Démarrez l'application web
CMD ["python3", "app.py"]

# Exposez le port 5000
EXPOSE 5000
