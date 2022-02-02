FROM python:3.10.1-alpine

ENV PORT 80
ENV FLASK_APP app

WORKDIR /app
COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:80", "flask_app" ]