# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
# TODO  https://perchrunway.com/blog/2017-01-19-getting-started-with-docker-for-local-development
FROM python:2.7

MAINTAINER Brian Ramsay "ramsayb2@berea.edu"

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt /tmp/pip-tmp/

RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

RUN bash -c "./setup.sh"

EXPOSE 8080
