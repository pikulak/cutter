#!/usr/bin/env bash

#wait until django do migrations
sleep 15

#wait until rabbitmq up
/wait-for-it.sh rabbitmq:5672 -t 0

cd cutter
celery -A cutter worker -B -l info