#!/bin/sh
DIR="$(dirname $(dirname $(readlink -f "$0")))"

docker run -it --rm \
        -v $DIR:/media \
        --workdir /media/src \
        --entrypoint bash \
        python:latest