####################################
# Image for develop                #
####################################

#FROM python:3.7-bullseye-slim as develop
FROM sphinxdoc/sphinx as develop
MAINTAINER Linkaform


ARG UID=${UID}
ARG GID=$UID

RUN groupadd -g "${UID}" sphinix \
  && useradd --create-home --no-log-init -u "${UID}" -g "${UID}" sphinix

USER sphinix

WORKDIR /srv/docs

ADD requirements.txt /srv/docs
RUN pip3 install -r requirements.txt

# Instala la librería sphinx-press-theme
RUN pip3 install sphinx-press-theme