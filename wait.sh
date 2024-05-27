#!/bin/bash

nohup redis-server &

#python3 /app/perf_processor/db_init.py
sleep 5

pushd /app
nohup flask run &
popd

sleep 3

/app/n9e webapi -c /app/etc/webapi.conf