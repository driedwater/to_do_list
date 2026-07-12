FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y docker.io

ENV DOCKER_HOST=tcp://host.docker.internal:2375

USER jenkins