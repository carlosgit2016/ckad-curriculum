FROM python:3.10.1-alpine

ENV MESSAGE message

WORKDIR /app
COPY ./src/ .
RUN ["pip", "install", "-r", "requirements.txt"] 
ENTRYPOINT [ "python", "main.py" ]