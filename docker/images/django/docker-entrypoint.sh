#!/bin/bash

# Stop on errors
set -eo pipefail

if [ "$TALOS_DATABASE_WAIT" ]; then
    while true
    do
        if python wait_for_dependencies.py
        then
            break
        fi
        echo 'Database is unavailable - sleeping'
        sleep 1
    done
fi

if [ "$TALOS_DATABASE_MIGRATE" ]; then
    python manage.py migrate --noinput
fi

exec "$@"
