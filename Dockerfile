# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
# TODO  https://perchrunway.com/blog/2017-01-19-getting-started-with-docker-for-local-development
FROM python:2.7

MAINTAINER Brian Ramsay "ramsayb2@berea.edu"

EXPOSE 8080

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

RUN ["/bin/bash","-c","./setup.sh"]

ENTRYPOINT [ "python", "api.py" ]
