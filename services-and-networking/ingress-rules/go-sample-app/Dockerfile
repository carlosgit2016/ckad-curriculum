FROM golang:alpine3.16 as app

WORKDIR /app
COPY . /app/

RUN go get . && \
    go build main

FROM alpine:3.16 as final
WORKDIR /app
COPY --from=app /app/index.html /app/index.html
COPY --from=app /app/main /app/main
CMD ["./main"]
