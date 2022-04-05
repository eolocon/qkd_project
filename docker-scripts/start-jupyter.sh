#!/bin/sh

if [ -z $1 ]; then
        echo "usage: $0 <image_name>"
        exit 0
fi

docker run -it --rm --publish 8888:8888 --hostname=jupyter $1 jupyter notebook --allow-root --ip=jupyter ./notebooks
