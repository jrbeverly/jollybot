#!/bin/sh
DIR="$(dirname $(dirname $(readlink -f "$0")))"

docker run -it --rm \
        -v $DIR:/media \
        --workdir /media/src \
        --entrypoint python3 \
        python:latest \
        main.py