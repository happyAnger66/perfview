#!/usr/bin/env bash

export FLASK_APP=app
export PYTHONPATH=$PYTHONPATH:.
#nohup flask run --host=172.19.0.1 & 2>&1
#python3 -m flask run --host=172.25.16.199
nohup flask run --host=172.25.8.123 & 2>&1
#flask run --host=192.168.100.253 
#docker run --network host --name p1 prom_proxy_20230307094147 flask run --host=172.25.8.123