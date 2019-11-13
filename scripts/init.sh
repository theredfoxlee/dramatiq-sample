#!/usr/bin/env bash

# initialize python environment
pip3 install virtualenv
python3 -m virtualenv env/
source env/bin/activate
pip install -r requirements.txt

# spawn rabbitmq
docker run \
    -d \
    --hostname rabbitmq \
    --name rabbitmq \
    -p 15672:15672 \
    -p 5672:5672 \
        rabbitmq:3.8.1-management

# spawn redis
docker run \
    -d \
    --hostname redis \
    --name redis \
    -p 6379:6379 \
        redis:5.0
