#!/bin/bash

# Stop on errors
set -eo pipefail

if [ -z "$HUB_HOST" ]; then
    echo 'HUB_HOST is undefined'
    exit 1
fi

if [ -z "$PROJECT_NAME" ]; then
    echo 'PROJECT_NAME is undefined'
    exit 1
fi

if [ -z "$PROJECT_VERSION" ]; then
    echo 'PROJECT_VERSION is undefined'
    exit 1
fi

habitus --keep-all --noprune-rmi \
    --build HUB_HOST=${HUB_HOST} \
    --build PROJECT_NAME=${PROJECT_NAME} \
    --build PROJECT_VERSION=${PROJECT_VERSION} \
    --build BUILD_DATE="`date -u +%Y-%m-%dT%H:%M:%SZ`" \
    --build GIT_COMMIT_ID="`git log -1 --pretty=format:'%H'`" \
    --build GIT_COMMIT_AUTHOR="`git log -1 --pretty=format:'%an'`" \
    --build GIT_COMMIT_CREATED="`git log -1 --pretty=format:'%cI'`" \
    --env HUB_HOST=${HUB_HOST} \
    --env PROJECT_NAME=${PROJECT_NAME} \
    --env PROJECT_VERSION=${PROJECT_VERSION} \
    "$@"
