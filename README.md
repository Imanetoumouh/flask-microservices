**Flask Microservice**

Ce projet est un microservice Flask qui utilise une base de données MySQL pour stocker des données d'utilisateurs. Le projet est divisé en quatre services :

* **db** : Service de base de données MySQL
* **html** : Service de stockage des fichiers HTML
* **web** : Service d'application web Flask

## Prérequis

Pour installer ce projet, vous devez disposer des éléments suivants :

* Docker
* Docker Compose

## Installation

Pour installer ce projet, suivez les étapes suivantes :

1. Créez un répertoire pour le projet :

```
mkdir flask-microservice
cd flask-microservice
```

2. Clonez le projet dans ce répertoire :

```
git clone https://github.com/Bard/flask-microservice.git
```

3. Ouvrez le fichier `docker-compose.yml` et modifiez le numéro de série du volume `mysql_data` pour correspondre au numéro de série de votre volume.

4. Exécutez la commande suivante pour construire les images Docker et exécuter les conteneurs :

```
docker-compose up
```

Une fois que les conteneurs sont en cours d'exécution, vous pouvez accéder à l'application web à l'adresse http://localhost:8080.

## Explication des services

Le service `db` est un service de base de données MySQL. Il utilise le volume `mysql_data` pour stocker les données de la base de données.

Le service `html` est un service de stockage des fichiers HTML. Il utilise le volume `html_data` pour stocker les fichiers HTML de l'application web.

Le service `web` est un service d'application web Flask. Il utilise le service `db` pour accéder à la base de données et le service `html` pour accéder aux fichiers HTML.

## Modification du projet

Pour modifier le projet, vous pouvez modifier les fichiers dans les répertoires `app`, `db`, `html`, et `web`.

Une fois que vous avez effectué des modifications, vous devez reconstruire les images Docker et redémarrer les conteneurs. Pour ce faire, exécutez les commandes suivantes :

```
docker-compose down
docker-compose up
```

## Problèmes courants

Si vous rencontrez des problèmes lors de l'installation ou de l'exécution du projet, vous pouvez consulter la documentation de Docker et de Docker Compose. Vous pouvez également consulter les journaux des conteneurs pour obtenir des informations sur les erreurs.

## Exemple de modification

Voici un exemple de modification que vous pouvez effectuer sur le projet :

Vous pouvez ajouter une nouvelle page HTML à l'application web. Pour ce faire, créez un nouveau fichier HTML dans le répertoire `html`. Ensuite, modifiez le code du service `web` pour charger la nouvelle page HTML.

Voici un exemple de code pour charger une nouvelle page HTML :

```python
from flask import render_template

@app.route("/new-page")
def new_page():
    return render_template("new-page.html")
```

Une fois que vous avez ajouté la nouvelle page HTML et modifié le code du service `web`, vous devez reconstruire les images Docker et redémarrer les conteneurs.

## Notes

* Le numéro de série du volume `mysql_data` est utilisé pour lier le volume Docker à un volume physique sur votre système. Vous pouvez trouver le numéro de série du volume physique en exécutant la commande `docker volume inspect mysql_data`.
* Vous pouvez accéder à la base de données MySQL en utilisant le client MySQL de votre choix. Le nom d'utilisateur et le mot de passe de la base de données sont définis dans le fichier `.env`.
* Vous pouvez modifier le code de l'application web pour ajouter de nouvelles fonctionnalités ou modifier le comportement de l'application.

**Versions**

* Version 1.0.0 (2023-11-15) : Version initiale

**Auteurs**

* Imane TOUMOUGH
