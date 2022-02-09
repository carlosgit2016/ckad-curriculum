FROM python:3.10.1-alpine

ENV PORT 80
ENV FLASK_APP app

WORKDIR /app
COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT [ "python", "-u", "flask_app.py" ]