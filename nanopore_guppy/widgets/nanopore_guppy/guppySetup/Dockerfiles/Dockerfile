FROM ubuntu:20.04
Maintainer lhhung
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get install -y \
        apt-transport-https \
        gnupg2 \
        software-properties-common curl\
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1 apt-key add - \
    && add-apt-repository -y \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable" \
    && apt-get update \
    && apt-get install -y \
        containerd.io \
        docker-ce \
        docker-ce-cli \
    && apt-get remove -y --purge --auto-remove \
        apt-transport-https \
        gnupg2 \
        software-properties-common \
    && rm -rf /var/lib/apt/lists/*
 WORKDIR /root/build
 COPY guppySetup.sh /usr/local/bin/guppySetup.sh
 COPY runGuppy.sh /root/build/runGuppy.sh
 COPY Dockerfile-gpu Dockerfile-gpu
