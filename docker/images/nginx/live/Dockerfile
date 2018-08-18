ARG PROJECT_VERSION
ARG HUB_HOST
ARG PROJECT_NAME

# Hack for use dynamically image tag
#FROM ${HUB_HOST}/${PROJECT_NAME}/nodejs-build:${PROJECT_VERSION} as nodejs-build

FROM ${HUB_HOST}/${PROJECT_NAME}/django:${PROJECT_VERSION} as django

FROM ${HUB_HOST}/${PROJECT_NAME}/nginx-base:${PROJECT_VERSION}

#COPY --from=nodejs-build /usr/local/code/build /usr/local/public/client

COPY --chown=nginx:nginx --from=django /usr/local/code/public/static /usr/local/public/static

ARG BUILD_DATE
ARG PROJECT_NAME

LABEL project.name=${PROJECT_NAME}
LABEL project.built=${BUILD_DATE}
