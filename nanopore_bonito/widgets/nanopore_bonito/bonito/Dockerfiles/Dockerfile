ARG VERSION=0.6.2
FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04
ARG VERSION
ENV DEBIAN_FRONTEND=noninteractive
#needed because NVIDIA decided to change the key for the CUDA repo
RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list
RUN apt-key del 7fa2af80
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub
#software-properties-common is needed for add-apt-repository
RUN apt-get update && apt-get install -y software-properties-common
#deadsnakes is needed for python3.10 and python headers are needed later for remora
RUN add-apt-repository ppa:deadsnakes/ppa && apt-get install -y git python3.10-dev curl apt-utils libz-dev
#install pip for python3.10 - the default install via python3-pip package installs pip requirements for python3.6 
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
#download bonito
RUN curl -s -L "https://github.com/nanoporetech/bonito/archive/refs/tags/v{$VERSION}.tar.gz" | tar -xz -C / && \
    mv /bonito-0.6.2 /bonito
#use the pip command directly instead through the usual ubuntu alias via python3.10 -m pip
RUN cd /bonito && \
    pip install -r requirements.txt && \ 
    python3.10 setup.py develop && \
    bonito download --models
    
RUN apt-get install -y bc
COPY runBonito.sh /usr/local/bin/runBonito.sh
