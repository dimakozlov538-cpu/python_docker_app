#!/bin/bash

docker build -t aboba-web .
docker rm -f web-container || true
docker run -d -p 80:8000 --name web-container aboba-web