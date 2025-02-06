# The first instruction is what image we want to base our container on
FROM mcr.microsoft.com/devcontainers/python:0-3.11

LABEL maintainer="Brian Ramsay 'ramsayb2@berea.edu'"

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

# Run source setup.sh whenever a bash terminal is opened in vscode (setup.sh is also run after volumes are mounted as the entrypoint in docker-compose)
RUN echo "source setup.sh > /dev/null" > /home/vscode/.bashrc

EXPOSE 8080
