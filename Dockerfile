FROM opencadc/astropy:3.8-slim

RUN apt-get update

RUN apt-get install -y \
    git 

RUN pip install cadcdata && \
    pip install cadctap && \
    pip install caom2 && \
    pip install caom2repo && \
    pip install caom2utils && \
    pip install deprecated && \
    pip install ftputil && \
    pip install importlib-metadata && \
    pip install pytz && \
    pip install PyYAML && \
    pip install spherical-geometry && \
    pip install vos

WORKDIR /usr/src/app

RUN pip install jsonpickle

ARG OPENCADC_BRANCH=master
ARG OPENCADC_REPO=opencadc
ARG OMC_REPO=opencadc-metadata-curation

RUN git clone https://github.com/${OPENCADC_REPO}/caom2tools.git --branch ${OPENCADC_BRANCH} --single-branch && \
    pip install ./caom2tools/caom2 && \
    pip install ./caom2tools/caom2utils

RUN git clone https://github.com/${OMC_REPO}/caom2pipe.git && \
  pip install ./caom2pipe

RUN git clone https://github.com/${OMC_REPO}/draost2caom2.git && \
  cp ./draost2caom2/scripts/config.yml / && \
  cp ./draost2caom2/scripts/docker-entrypoint.sh / && \
  pip install ./draost2caom2

ENTRYPOINT ["/docker-entrypoint.sh"]
