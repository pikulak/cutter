#!/usr/bin/env bash

#wait until django do migrations
sleep 25

#wait until rabbitmq up
/wait-for-it.sh rabbitmq:5672 -t 0

cd cutter
celery -A cutter worker -l info