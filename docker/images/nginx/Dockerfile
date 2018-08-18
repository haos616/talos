FROM nginx:1.14.0

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    python \
    python-pip \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/{apt,dpkg,cache,log}

ADD ./files/ /usr/local/docker/

RUN mv /usr/local/docker/nginx.conf /etc/nginx/nginx.conf \
    && chmod +x /usr/local/docker/docker-entrypoint.sh

RUN pip install --no-cache-dir -U setuptools \
    && pip install --no-cache-dir -r /usr/local/docker/requirements.txt

ENTRYPOINT ["/usr/local/docker/docker-entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]
