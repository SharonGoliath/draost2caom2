FROM python:3.6-alpine

RUN apk --no-cache add \
    bash \
    coreutils \
    gcc \
    git \
    g++ \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    make \
    musl-dev \
    openssl-dev

RUN pip install aenum && \
    pip install astropy && \
    pip install cadcdata && \
    pip install cadctap && \
    pip install caom2repo && \
    pip install funcsigs && \
    pip install future && \
    pip install numpy && \
    pip install PyYAML && \
    pip install spherical-geometry && \
    pip install vos && \
    pip install xml-compare

RUN git clone https://github.com/opencadc-metadata-curation/caom2tools.git && \
  cd caom2tools && git pull origin master && \
  pip install ./caom2utils && pip install ./caom2pipe && cd ..

RUN git clone https://github.com/opencadc-metadata-curation/draost2caom2.git && \
  cp ./draost2caom2/scripts/config.yml / && \
  cp ./draost2caom2/scripts/docker-entrypoint.sh / && \
  pip install ./draost2caom2

RUN apk --no-cache del git

ENTRYPOINT ["/docker-entrypoint.sh"]


