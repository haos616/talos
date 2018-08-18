FROM debian:9.4

RUN apt update \
    && apt install --no-install-recommends -y git \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/

ADD https://github.com/cloud66/habitus/releases/download/1.0.3/habitus_linux_amd64 /usr/local/bin/habitus

RUN sha1sum /usr/local/bin/habitus \
    && echo '13c9bbdaedcaf00b3fc29c731b9b042a413c84dd /usr/local/bin/habitus' | sha1sum -c - \
    && chmod +x /usr/local/bin/habitus

ADD docker-entrypoint.sh /usr/local/docker/docker-entrypoint.sh

RUN chmod +x /usr/local/docker/docker-entrypoint.sh

ENTRYPOINT ["/usr/local/docker/docker-entrypoint.sh"]

CMD ["habitus"]
