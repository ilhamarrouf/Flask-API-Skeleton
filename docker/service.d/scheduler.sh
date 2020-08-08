#!/usr/bin/env bash

# Init vars
# init in here....

exec /bin/sh -c "while [ true ]; do (python /app/scheduler.py --verbose --no-interaction &); sleep 60; done"
