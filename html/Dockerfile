# Dockerfile pour les fichiers HTML
# Ce Dockerfile sera basé sur l'image officielle de Nginx Docker

FROM nginx:1.21.6

# Copiez les fichiers HTML dans le conteneur
COPY registration.html /usr/share/nginx/html/registration.html
COPY index.html /usr/share/nginx/html/index.html

# Démarrez Nginx
CMD ["nginx", "-g", "daemon off;"]