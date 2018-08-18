FROM python:3.6.6

ENV DOCKER_USER_ID 1000
ENV DOCKER_GROUP_ID 1000

ENV PYTHONUNBUFFERED 1

RUN groupadd -g ${DOCKER_GROUP_ID} user \
    && useradd --shell /bin/bash -u $DOCKER_USER_ID -g $DOCKER_GROUP_ID -o -c "" -m user

ADD --chown=user:user ./server/requirements.txt ./server/wait_for_dependencies.py /usr/local/code/

ADD --chown=user:user ./docker/images/django/docker-entrypoint.sh /usr/local/docker/docker-entrypoint.sh

RUN chmod +x /usr/local/docker/docker-entrypoint.sh \
    && pip install --no-cache-dir -U pip setuptools \
    && pip install --no-cache-dir -r /usr/local/code/requirements.txt

WORKDIR /usr/local/code

VOLUME ["/usr/local/code/public/media/"]

USER user

EXPOSE 8000

ENTRYPOINT ["/usr/local/docker/docker-entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
