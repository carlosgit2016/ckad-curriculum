FROM debian:stable-20220622-slim

RUN apt-get update && \
    apt-get install python3-minimal -y && \
    apt-get install python3-pip -y

WORKDIR /app
COPY . ./

RUN pip install --user pipenv
ENV PATH $PATH:/root/.local/bin/
RUN pipenv --python /usr/bin/python3 install -d

ENV VERSION 0.0.1
ENV PORT 8080

ENTRYPOINT ["pipenv", "run", "prod"]