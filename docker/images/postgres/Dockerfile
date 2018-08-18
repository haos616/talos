FROM postgres:10.4

# Install postgis extension
#RUN apt-get update \
#    && apt-get install --no-install-recommends -y postgresql-10-postgis-2.4 postgresql-10-postgis-2.4-scripts  \
#    && apt-get clean autoclean \
#    && apt-get autoremove -y \
#    && rm -rf /var/lib/{apt,dpkg,cache,log}

# Add backup scripts
ADD ./backup.sh /usr/local/bin/backup
ADD ./restore.sh /usr/local/bin/restore
ADD ./list-backups.sh /usr/local/bin/list-backups

# Make them executable
RUN chmod +x /usr/local/bin/restore \
    && chmod +x /usr/local/bin/list-backups \
    && chmod +x /usr/local/bin/backup

# Add script create extension
#ADD ./create-extension.sh /docker-entrypoint-initdb.d/create-extension.sh

ADD ./docker-entrypoint.sh /usr/local/docker/docker-entrypoint.sh


ARG BUILD_DATE
ARG PROJECT_NAME

LABEL project.name=${PROJECT_NAME}
LABEL project.built=${BUILD_DATE}
