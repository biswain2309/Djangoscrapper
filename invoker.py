import time
# from tasks import add
from tasks import data_extractor
from celery.result import AsyncResult

#Producer part of code
# result = add.delay(1,2)

data_extractor.delay()

# while True:
#     _result2 = AsyncResult(result.task_id)
#     status = _result2.status
#     print(status)
#     if 'SUCCESS' in status:
#         print('result after 5 sec wait {_result2}'.format(_result2=_result2.get()))
#         break
#     time.sleep(5)