#!/bin/sh

if [ -z $1 ] || [ -z $2 ]; then
        echo "usage: $0 <image_name> <port>"
        exit 0
fi

docker run -it --rm --publish $2:$2 --hostname=localhost $1 jupyter notebook --allow-root --no-browser --port=$2 --ip=localhost ./notebooks
