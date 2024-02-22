# Utilise une image de base Python
FROM python:3.12.1-alpine
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

# Exposez le port sur lequel votre application s'exécute
EXPOSE 5000

# Définissez la commande pour exécuter votre application
CMD ["python", "flaskapp.py"]
