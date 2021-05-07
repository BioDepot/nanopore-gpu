FROM alpine:3.13.2
RUN adduser --disabled-password -s /bin/bash user
RUN apk add --update --no-cache bash curl wget
COPY download.sh /root
