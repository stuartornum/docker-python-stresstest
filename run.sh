#!/bin/bash

service nginx start
cd /srv/
gunicorn -w 4 -b 127.0.0.1:8001 hello:app

