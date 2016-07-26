from __future__ import absolute_import

from mysite.celery import app


@app.task()
def add(x, y):
    return int(x) + int(y)


@app.task()
def mul(x, y):
    return int(x) * int(y)


@app.task()
def xsum(numbers):
    return sum(numbers)
