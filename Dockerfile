####################################
# Image for develop                #
####################################

#FROM python:3.7-bullseye-slim as develop
FROM sphinxdoc/sphinx as develop

MAINTAINER Linkaform

WORKDIR /srv/docs

ADD requirements.txt /srv/docs
RUN pip3 install -r requirements.txt