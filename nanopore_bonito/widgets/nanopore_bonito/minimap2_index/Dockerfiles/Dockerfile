FROM debian:buster-slim as builder 
ARG TARGETARCH
ARG MINIMAP2_VER="2.24"
ARG SAMTOOLS_VER="1.16.1"
RUN apt-get update && apt-get install -y curl bzip2 build-essential g++ libbz2-dev libz-dev ncurses-dev liblzma-dev libcurl4-openssl-dev 
RUN curl -L https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}.tar.bz2 | tar -jxvf - 
RUN if [ "$TARGETARCH" = "arm64" ] ; then cd minimap2-${MINIMAP2_VER} && make arm_neon=1 aarch64=1; else cd minimap2-${MINIMAP2_VER} && make ; fi
RUN curl -L https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 | tar -jxvf - 
RUN cd samtools-${SAMTOOLS_VER} && make -j8

FROM debian:buster-slim
ARG MINIMAP2_VER="2.24"
ARG SAMTOOLS_VER="1.16.1"
RUN apt-get update && apt-get install -y libbz2-dev libz-dev ncurses-dev liblzma-dev libcurl4-openssl-dev
COPY --from=builder minimap2-${MINIMAP2_VER}/minimap2 /usr/local/bin/minimap2
COPY --from=builder samtools-${SAMTOOLS_VER}/samtools /usr/local/bin/samtools 
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/local/bin:${PATH}"
COPY runIndex.sh /usr/local/bin/runIndex.sh
