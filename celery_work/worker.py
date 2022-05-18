import time
from celery import Celery


app = Celery(
    broker_url = "redis://:bsIwj0mAE3zODIm3irCJjn4KVAfWDfBp@redis-18506.c299.asia-northeast1-1.gce.cloud.redislabs.com:18506"
)

app.conf.update(
    task_serializer = "json",
    result_serializer = "json",
    task_ignore_result = True,
)


@app.task(name="new_task")
def new_task(text: str) -> bool:
    time.sleep(5)
    with open("readme.txt", "a") as f:
        f.write(text)
    return True