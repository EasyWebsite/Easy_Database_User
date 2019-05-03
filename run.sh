#!/bin/bash

is_ready() {
    eval "curl -I http://${RABBIT_USER}:${RABBIT_PASSWORD}@${RABBIT_HOST}:${RABBIT_MANAGEMENT_PORT}/api/vhosts"
}

i=0
while ! is_ready; do
    i=`expr $i + 1`
    if [ $i -ge 10 ]; then
        echo "$(date) - rabbit still not ready, giving up"
        exit 1
    fi
    echo "$(date) - waiting for rabbit to be ready"
    sleep 3
done

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000