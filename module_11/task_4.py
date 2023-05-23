import queue
import random
import threading
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Task:
    def __init__(self, priority: int, time_sleep: float):
        self.priority = priority
        self.time_sleep = time_sleep

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        time.sleep(self.time_sleep)
        return f'Task(priority={self.priority}) ------  sleep({self.time_sleep})'


class Producer(threading.Thread):
    def __init__(self, queue: queue.PriorityQueue, count: int):
        super().__init__()
        self.queue = queue
        self.count = count
        logger.info('Producer: Running')

    def run(self):
        for i in range(self.count):
            priority = random.randint(0, 6)
            task = Task(priority, random.random())
            self.queue.put((priority, task))
        consumer = Consumer(self.queue)
        consumer.start()
        consumer.join()
        logger.info('Producer: Done')


class Consumer(threading.Thread):
    def __init__(self, queue: queue.PriorityQueue):
        super().__init__()
        self.queue = queue
        self.tasks_done = 0
        logger.info('Consumer: Running')

    def run(self):
        while True:
            priority, task = self.queue.get()
            logger.info(f'>running {task}')
            self.queue.task_done()
            self.tasks_done += 1
            if self.queue.empty():
                logger.info('Consumer: Done')
                break


def main():
    _queue = queue.PriorityQueue()
    producer = Producer(_queue, 5)
    producer.start()
    _queue.join()
    producer.join()


if __name__ == '__main__':
    main()
