
FROM ubuntu:14.10

ENV MCLOUD_VERSION 0.10.1
ENV DOCKER_MACHINE_VER v0.3.0

RUN apt-get update && apt-get install -y \
    redis-server python-dev python-pip libffi-dev \
    python-virtualenv libssl-dev libncurses5-dev libreadline-dev curl libyaml-dev rsync vim curl supervisor

RUN mkdir /etc/mcloud && virtualenv /opt/mcloud

RUN /opt/mcloud/bin/pip install mcloud supervisor-stdout
RUN ln -s /opt/mcloud/bin/mcloud* /usr/bin/ && \
    ln -s /opt/mcloud/bin/pip /usr/bin/mcloud-plugins


RUN curl -L https://github.com/docker/machine/releases/download/$DOCKER_MACHINE_VER/docker-machine_darwin-amd64 > /usr/local/bin/docker-machine
RUN chmod +x /usr/local/bin/docker-machine

COPY mcloud-server.yml /etc/mcloud/mcloud-server.yml
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN ln -sf /bin/bash /bin/sh
ENV PS1 "\[\e[34;46m\][mcloud] \w\[\e[m\]\[\e[34;46m\]\$\[\e[m\]\[\e[46m\] \[\e[m\] "

# simplify mcloud development
VOLUME /opt/mcloud/local/lib/python2.7/site-packages/mcloud


# supervisor
RUN pip install

CMD ["/usr/bin/supervisord"]
