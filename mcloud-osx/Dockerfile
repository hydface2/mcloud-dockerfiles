
FROM mcloud/mcloud

VOLUME /Users

RUN /opt/mcloud/bin/pip install pynetinfo

ENV DOCKER_TLS_VERIFY="1" \
    DOCKER_HOST="tcp://*:2376" \
    DOCKER_CERT_PATH="/Users/*/.docker/machine/machines/dev" \
    DOCKER_MACHINE_NAME="dev" \
    MCLOUD_USE_DOCKER_MACHINE="1"


ADD mcloud-server.yml /etc/mcloud/mcloud-server.yml

EXPOSE 80

ENV MCLOUD_HOST="127.0.0.1:80"


