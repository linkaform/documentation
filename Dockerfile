####################################
# Image for develop                #
####################################

#FROM python:3.7-bullseye-slim as develop
FROM sphinxdoc/sphinx as develop
MAINTAINER Linkaform


RUN apt-get update && \
    apt-get install -y \
    graphviz

ARG UID=${UID}
ARG GID=${UID}
ARG UID=1000
ARG GID=1000


RUN groupadd -g $GID sphinix 
RUN useradd --create-home --no-log-init -u $GID -g $GID sphinix

USER sphinix

WORKDIR /srv/docs

ADD requirements.txt /srv/docs
RUN pip3 install -r requirements.txt
