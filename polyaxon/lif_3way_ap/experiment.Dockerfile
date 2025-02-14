FROM registry.aisingapore.net/polyaxon/cuda10:latest

ARG USER="polyaxon"
ARG WORK_DIR="/home/$USER"

RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \
    apt update && apt install -y jq ca-certificates

WORKDIR $WORK_DIR
USER $USER

COPY build/polyaxon/lif_3way_ap/conda.yml .
COPY build/sgnlp_models/models/lif_3way_ap/requirements.txt .
RUN conda env update -f conda.yml -n base
RUN python -m spacy download en_core_web_sm

WORKDIR /code

COPY --chown=$USER:$USER build .

ENV LD_LIBRARY_PATH /usr/local/cuda/lib64:$LD_LIBRARY_PATH