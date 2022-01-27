FROM python:3.10.1-alpine

ENV LOGS_PATH /var/logs
ENV LOGS_PREFIX "[APP<number>] [WARN]"

WORKDIR /app
COPY main.py .

ENTRYPOINT [ "python", "main.py" ]