import time
import threading
import random
import queue

#TASK1: Basic concepts of Threading 

# def countdown(count):
#     while(count >= 0):
#         print("{} Counting down buddy! {}".format(threading.current_thread(), count))
#         count -= 1
#         time.sleep(3)

# def countup(count):
#     while(count >= 0):
#         print("{} Counting up buddy! {}".format(threading.current_thread(), count))
#         count += 1
#         time.sleep(5)

# t1 = threading.Thread(name="countdown", args=(10,), target=countdown)
#t1.start()

# t2 = threading.Thread(name="countup", args=(0,), target=countup)
#t2.start()

#print("All done!")


#TASK2: Solving Consumer roducers problem ith Mutual Exclusion

# counter_buffer = 0
# counter_lock = threading.Lock()
# COUNTER_MAX = 100000

# def consumer1_counter():
#     global counter_buffer
#     for i in range(COUNTER_MAX):
#         counter_lock.acquire()
#         counter_buffer += 1
#         counter_lock.release()


# def consumer2_counter():
#     global counter_buffer
#     for i in range(COUNTER_MAX):
#         counter_lock.acquire()
#         counter_buffer += 1
#         counter_lock.release()

# t1 = threading.Thread(target=consumer1_counter)
# t2 = threading.Thread(target=consumer2_counter)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(counter_buffer)

#TASK3: Controlling threads with conditions. Consumers should not access the buffer when it is empty. 
# Producer will notify the Threads when it dumps data into Shared resources.

##Learning: Whenever a multi threading program executes continuously without stopping, we must ensure
#that the main thread is never sleeping and all the other threads are deamonized.
#And when main program exits, associated daemon threads are killed too.

_queue = queue.Queue(10)

condition = threading.Condition()

class ProducerThread(threading.Thread):
    def run(self):
        numbers = range(5)
        global _queue

        while True:
            number = random.choice(numbers)
            _queue.put(number)
            print('Produced {}'.format(number))
            time.sleep(random.random())

class ConsumerThread(threading.Thread):

    def run(self):
        global _queue
        while True:
            if not _queue:
                print("Nothing in queue, Consumer is waiting")
                print("Producer added soemthing to queue and notify the consumer")
            
            number = _queue.get()
            _queue.task_done()
            print("Consumed {}".format(number))
            time.sleep(random.random())

producer = ProducerThread()
producer.daemon = True
producer.start()

consumer = ConsumerThread()
consumer.daemon = True
consumer.start()

while True:
    time.sleep(1)


#Learning: using daemon thread the main thread can completely forget about this task and this 
# task will either complete or killed when main thread exits.

#Note that you should use daemon thread only for non essential tasks that you don’t mind if it 
# doesn’t complete or left in between.





