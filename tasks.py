import time
from celery import Celery

app = Celery('tasks', backend = 'redis://localhost:6379/0', broker = 'redis://localhost:6379/0')

##Consumer part of code
# @app.task(name='tasks.add')
# def add(x, y):
#     total = x + y
#     print('{} + {} = {}'.format(x, y, total))
#     time.sleep(10)
#     return total


#Exception handling in Celery

##Exponential backoff
def backoff(attempts):
    """
    1,2,4,8,16,32,...
    """
    return 2 ** attempts


@app.task(bind=True, max_retries=4)
def data_extractor(self):
    try:
        for i in range(1,11):
            print('Crawling HTML DOM!')
            if i == 5:
                raise ValueError('Crwaling Index Error')
    except Exception as exc:
        print('Lets retry after 5 seconds')
        raise self.retry(exc=exc, countdown=backoff(self.request.retries))