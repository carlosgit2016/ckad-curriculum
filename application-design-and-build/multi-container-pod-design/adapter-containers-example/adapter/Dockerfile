FROM python:3.10.1-alpine

WORKDIR /app
COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT [ "python", "-u", "main.py" ]
