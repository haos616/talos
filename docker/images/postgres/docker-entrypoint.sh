#!/bin/bash

# Stop on errors
set -eo pipefail

USER_ID=${LOCAL_USER_ID:-1000}

echo "Starting with UID : $USER_ID"
useradd --shell /bin/bash -u $USER_ID -o -c "" -m user || echo "User already exists"
export HOME=/home/user

chown "$USER_ID":"$USER_ID" /backups -R

gosu user "$@"
