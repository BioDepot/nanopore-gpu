FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y python3-pip git python3.6

RUN apt-get install -y libz-dev && \
    git clone https://github.com/nanoporetech/bonito.git && \
    cd bonito && \
    sed -i 's/torch==1.8.0/torch==1.7.1/g' requirements.txt && \
    pip3 install -r requirements.txt && \
    python3 setup.py develop && \
    bonito download --models
    
RUN apt-get install -y bc
COPY runBonito.sh /usr/local/bin/runBonito.sh
