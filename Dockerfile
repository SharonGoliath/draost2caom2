FROM opencadc/astropy:3.8-slim

RUN apt-get update -y && apt-get dist-upgrade -y

RUN apt-get install -y \
    git \
    python3-pip \
    python3-tz \
    python3-yaml

RUN pip3 install cadcdata && \
    pip3 install cadctap && \
    pip3 install caom2 && \
    pip3 install caom2repo && \
    pip3 install caom2utils && \
    pip3 install deprecated && \
    pip3 install ftputil && \
    pip3 install importlib-metadata && \
    pip3 install pytz && \
    pip3 install PyYAML && \
    pip3 install spherical-geometry && \
    pip3 install vos

WORKDIR /usr/src/app

RUN pip3 install jsonpickle

ARG OMC_REPO=opencadc-metadata-curation

RUN git clone https://github.com/${OMC_REPO}/caom2pipe.git && \
  pip install ./caom2pipe

RUN git clone https://github.com/${OMC_REPO}/draost2caom2.git && \
  cp ./draost2caom2/scripts/config.yml / && \
  cp ./draost2caom2/scripts/docker-entrypoint.sh / && \
  pip install ./draost2caom2

ENTRYPOINT ["/docker-entrypoint.sh"]
