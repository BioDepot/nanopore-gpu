FROM alpine:3.12.1
MAINTAINER Hong Hung
RUN apk update upgrade --no-cache && apk add bash jq rsync && rm -rf /var/cache/apk*
COPY start.sh /usr/local/bin/.
