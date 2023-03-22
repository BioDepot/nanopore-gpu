ARG VERSION=0.6.2
FROM nvidia/cuda:11.3.0-runtime-ubuntu20.04
ARG VERSION
ENV DEBIAN_FRONTEND=noninteractive
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

RUN apt-get update && apt-get install -y python3 python3-pip curl zlib1g-dev libbz2-dev liblzma-dev bc \
    && curl -s -L "https://github.com/nanoporetech/bonito/archive/refs/tags/v{$VERSION}.tar.gz" | tar -xz -C / \
    && mv /bonito-0.6.2 /bonito \
    && cd /bonito  \
    && python3 -m pip install -r requirements.txt \ 
    && python3 setup.py develop \
    && bonito download --models \
    && cd / && rm -r /bonito \
    && rm -rf /var/lib/apt/lists/*

COPY runBonito.sh /usr/local/bin/runBonito.sh
