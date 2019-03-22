FROM ubuntu:18.04

MAINTAINER wangwukong

COPY .docker /.docker

WORKDIR /.docker

# 更换软件源
RUN mv sources.list /etc/apt/ && \
    apt-get update && \
    apt-get install python python3 git wget gcc make -y

CMD bash -i