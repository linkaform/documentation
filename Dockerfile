####################################
# Image for develop                #
####################################

#FROM python:3.7-bullseye-slim as develop
FROM sphinxdoc/sphinx as develop
MAINTAINER Linkaform

ARG UID=1000
ARG GID=1000

RUN groupadd -g "${GID}" sphinix \
  && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" sphinix

USER sphinix

WORKDIR /srv/docs

ADD requirements.txt /srv/docs
RUN pip3 install -r requirements.txt