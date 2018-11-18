#! /bin/bash

docker build -t bomblab .
docker run -p 127.0.0.1:9898:9898 -ti -d bomblab
