#!/usr/bin/env bash

#wait until django do migrations
sleep 15

#wait until rabbitmq up
/wait-for-it.sh rabbitmq:5672

cd simple_site_requester
celery -A simple_site_requester worker -B -l info