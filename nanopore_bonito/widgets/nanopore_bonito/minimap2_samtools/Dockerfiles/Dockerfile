FROM debian:buster-slim
Maintainer Shishir Reddy
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/local/bin:${PATH}"
RUN apt-get update && apt install -y minimap2 samtools
COPY runMiniMap2.sh /usr/local/bin/runMiniMap2.sh
