import os
import time
import requests
import json

from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = "redis://:bsIwj0mAE3zODIm3irCJjn4KVAfWDfBp@redis-18506.c299.asia-northeast1-1.gce.cloud.redislabs.com:18506"
# redis://:password@hostname:port/db_number

@celery.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True


@celery.task(name="new_task")
def new_task(task):
    with open('readme.txt', 'a') as f:
        f.write(str(task))
    # payload = {
    #     "text": task
    # }
# 
    # r = requests.post("http://0.0.0.0:5000/new", data=json.dumps(payload))
    return True

# payload = {
#     "text": "blablabla"
# }
# 
# r = requests.post("http://0.0.0.0:5000/new", data=json.dumps(payload))
# print(r.text)