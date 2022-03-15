#!/bin/sh

docker run -it --rm --publish 8888:8888 --hostname=jupyter tesi-project jupyter notebook --allow-root --ip=jupyter ./notebooks