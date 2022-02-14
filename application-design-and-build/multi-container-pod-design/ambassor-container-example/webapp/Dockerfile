FROM python:3.10.1-alpine

ENV PORT 80

WORKDIR /app
COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT [ "python", "-u", "app.py" ]