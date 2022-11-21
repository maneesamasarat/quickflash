#!/bin/bash
killall -s 15 celery
killall -s 15 python
sudo redis-cli flushall
sudo service redis-server stop