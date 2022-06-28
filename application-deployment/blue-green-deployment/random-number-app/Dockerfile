FROM debian:stable-20220622-slim

RUN apt update && \
    apt install python3-minimal -y && \
    apt install python3-pip -y

WORKDIR /app
COPY *.py ./
COPY *.txt ./

RUN pip install -r "requirements.txt" -t "." --ignore-installed

ENV VERSION 0.0.1
ENV PORT 8080

ENTRYPOINT ["python3", "-u", "/app/main.py"]