# syntax = docker/dockerfile:1.2

# Utilise une image de base Python built for the linux/amd64 platform (render.com requirement)
FROM --platform=linux/amd64 python:3.12-alpine

# Set the timezone to Europe/Paris
ENV TZ=Europe/Paris

#copy the content of my current directory in my local system to a new directory named app in the docker image file system
COPY . /app

# Copy the SSL certificate file
COPY cacert-2023-12-12.pem /etc/secrets/cacert-2023-12-12.pem

#Définit le répertoire de travail
WORKDIR /app

# Install necessary dependencies
RUN apk update && \
    apk add --no-cache gcc musl-dev mariadb-connector-c-dev pkgconf prometheus-client

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose le port sur lequel l'application s'exécute
EXPOSE 5000

# Définit la commande pour exécuter l'application
CMD ["python", "flaskapp.py"]
