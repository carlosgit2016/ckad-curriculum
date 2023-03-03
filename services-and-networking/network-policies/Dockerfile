FROM alpine:3.16

RUN apk update && \
    apk add curl \
    bind-tools \
    coreutils \
    jq \
    busybox-extras

ENTRYPOINT ["/bin/sh", "-c"]
CMD ["tail -f /dev/null"]
