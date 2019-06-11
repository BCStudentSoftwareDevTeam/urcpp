# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:2.7

MAINTAINER Guillermo Ramos "guillermoramos330179@gmail.com"

EXPOSE 80

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /
ENTRYPOINT [ "python" ]

CMD [ "api.py" ]
