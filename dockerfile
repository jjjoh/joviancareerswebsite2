FROM python:3.12.1
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt