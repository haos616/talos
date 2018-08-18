ARG PROJECT_VERSION
ARG HUB_HOST
ARG PROJECT_NAME

FROM ${HUB_HOST}/${PROJECT_NAME}/django-base:${PROJECT_VERSION}

ADD --chown=user:user ./server /usr/local/code

RUN python -m compileall /usr/local/code \
    && cp /usr/local/code/talos/settings/envs/.env.fake /usr/local/code/talos/settings/.env \
    && python manage.py collectstatic --noinput \
    && rm /usr/local/code/talos/settings/.env

CMD ["gunicorn", "-b", "0.0.0.0:8000", "talos.wsgi:application", "-w", "1"]


ARG GIT_COMMIT_ID=unknown
ARG GIT_COMMIT_AUTHOR=unknown
ARG GIT_COMMIT_CREATED=unknown

ENV GIT_COMMIT_ID=${GIT_COMMIT_ID}
ENV GIT_COMMIT_AUTHOR=${GIT_COMMIT_AUTHOR}
ENV GIT_COMMIT_CREATED=${GIT_COMMIT_CREATED}


ARG BUILD_DATE
ARG PROJECT_NAME

LABEL project.name=${PROJECT_NAME}
LABEL project.built=${BUILD_DATE}
