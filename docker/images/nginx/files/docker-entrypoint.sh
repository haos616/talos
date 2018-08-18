#!/bin/bash
cd /usr/local/docker

python generate.py && exec "$@"
