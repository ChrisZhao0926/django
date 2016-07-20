from celery import Celery

app = Celery('new_tasks', backend='rpc://', broker='amqp://')


@app.task()
def sub(x, y):
    return int(x) - int(y)
