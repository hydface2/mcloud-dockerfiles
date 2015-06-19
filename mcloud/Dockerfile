
FROM ubuntu-upstart:14.10

RUN apt-get update && apt-get install -y \
    redis-server python-dev python-pip libffi-dev \
    python-virtualenv libssl-dev libncurses5-dev libreadline-dev libyaml-dev

RUN mkdir /etc/mcloud && virtualenv /opt/mcloud

RUN /opt/mcloud/bin/pip install mcloud
RUN ln -s /opt/mcloud/bin/mcloud* /usr/bin/ && \
    ln -s /opt/mcloud/bin/pip /usr/bin/mcloud-plugins

ADD upstart.conf /etc/init/mcloud.conf
ADD mcloud-server.yml /etc/mcloud/mcloud-server.yml

RUN echo 'root:mcloud.io' | chpasswd
RUN ln -sf /bin/bash /bin/sh
ENV PS1 "\[\e[34;46m\][mcloud] \w\[\e[m\]\[\e[34;46m\]\$\[\e[m\]\[\e[46m\] \[\e[m\] "

RUN apt-get update && apt-get install -y rsync vim

# simplify mcloud development
VOLUME /opt/mcloud/local/lib/python2.7/site-packages/mcloud