# Dockerfile pour la base de données MySQL
# Ce Dockerfile sera basé sur l'image officielle de MySQL Docker

FROM mysql:5.7

RUN apt-get update && apt-get install -y mysql-client


# Définit l'hôte de la base de données
ENV DATABASE_HOST=localhost
# Définit le port de la base de données
ENV DATABASE_PORT=3306
# Définit le nom de la base de données
ENV DATABASE_NAME=devops
# Définit l'utilisateur de la base de données
ENV DATABASE_USER=root
# Définit le mot de passe de la base de données
ENV DATABASE_PASSWORD=
# Définit le mot de passe root de la base de données
#ENV MYSQL_ROOT_PASSWORD=


EXPOSE 3306 

# Démarrez le serveur MySQL
CMD ["mysqld"]