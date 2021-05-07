FROM debian:buster-slim
Maintainer Shishir Reddy
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt install -y minimap2
COPY runIndex.sh /usr/local/bin/runIndex.sh
