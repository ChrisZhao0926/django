from celery import Celery

app = Celery('mytasks', backend='rpc://', broker='amqp://')


@app.task()
def sub(x, y):
    return int(x) - int(y)


@app.task()
def add(x, y):
    return int(x) + int(y)

