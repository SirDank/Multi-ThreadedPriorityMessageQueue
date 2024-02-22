import time
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor
from dankware import clr, cls, green_bright, white_bright, reset

# Constants
SLEEP_INTERVAL = 0.1

# Classes
class UserThread:
    def __init__(self):
        self.inbox = []
        self.id = thread_id(current_thread().name)
        threads[self.id] = self # pylint: disable=used-before-assignment
        self.worker()

    def get_msg(self, sender: str, msg: str):
        self.inbox.append((sender, msg))

    def send_msg(self, receiver: str, priority: int, msg: str):
        queue.append((priority, self.id, receiver, msg)) # pylint: disable=used-before-assignment

    def worker(self):
        print(clr(f"  - [{self.id}] joined!", colour_one=green_bright, colour_two=white_bright))
        while running: # pylint: disable=used-before-assignment
            if self.inbox:
                sender, msg = self.inbox.pop()
                print(clr(f"  - [{sender}]>[{self.id}]: {msg}", colour_two=green_bright))
            time.sleep(SLEEP_INTERVAL)

# Helper functions
def thread_id(name: str) -> str:
    return name.replace('ThreadPoolExecutor-0_', 'T')

def queue_not_empty() -> bool:
    return bool(queue)

def dequeue() -> tuple:
    top_priority = 0
    for index, task in enumerate(queue):
        if task[0] > top_priority:
            top_priority = task[0]
            top_index = index
    return queue.pop(top_index)

def peak() -> None:
    if queue_not_empty():
        top_priority = 0
        for task in queue:
            if task[0] > top_priority:
                top_priority = task[0]
                top_task = task
        print(clr(f"  - Top task: {top_task}", colour_one=green_bright, colour_two=white_bright))
    else:
        print(clr("  - Queue is empty!",2))

# Message handler
def message_handler():
    print(clr(f"  - [{thread_id(current_thread().name)}] Message handler started!", colour_one=green_bright, colour_two=white_bright))
    while running:
        if queue_not_empty():
            task = dequeue()
            if task[1] == task[2]:
                # thread kill could be implemented here if spamming continues
                print(clr(f"  - [{task[1]}] tried to send a message to itself!",2))
            elif task[2] not in threads:
                print(clr(f"  - [{task[1]}] tried to send a message to a non-existent thread [{task[2]}]!",2))
            else:
                threads[task[2]].get_msg(task[1], task[3])
        time.sleep(SLEEP_INTERVAL)

# Main
if __name__ == "__main__":

    cls()
    queue = [] # (priority, sender, receiver, msg)
    running = True
    threads = {}
    max_threads = int(input(clr("  > Enter the number of threads / users: ", colour_two=green_bright) + green_bright)); print(reset)

    # Start int(threads) number of UserThreads and 1 message_handler thread
    executor = ThreadPoolExecutor(max_threads+1)
    executor.submit(message_handler)
    for _ in range(max_threads):
        executor.submit(UserThread)

    # Enqueue implementation
    time.sleep(2) # example part 1
    threads['T1'].send_msg('T2', 1, 'Hey T2, how ya been?') # lowest priority, will be sent last
    threads['T1'].send_msg('T3', 2, 'Long time no see, T3!')
    threads['T3'].send_msg('T1', 3, 'Been a while T1, hope you\'re well :)') # highest priority, will be sent first
    peak()

    time.sleep(2) # example part 2
    threads['T1'].send_msg('T1', 1, 'I am talking to myself (clearly delulu)')
    threads['T1'].send_msg('T1', 1, 'I am sending a message to myself a second time?! (going insane)')
    threads['T1'].send_msg('T1', 1, 'I am sending a message to myself a third time?! (call 4 help pls)')

    time.sleep(2) # example part 3
    threads['T2'].send_msg('T420', 1, 'Do you exist?')
    threads['T2'].send_msg('T420', 1, 'Yooooooooo')

    time.sleep(5)
    running = False
    #executor.shutdown() # not needed!
