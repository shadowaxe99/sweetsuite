```python
import queue
from threading import Thread
from email_sender import send_email

class EmailQueue:
    def __init__(self):
        self.email_queue = queue.Queue(maxsize=1000)
        self.worker_thread = Thread(target=self.__worker)
        self.worker_thread.start()

    def add_to_queue(self, email_data):
        self.email_queue.put(email_data)

    def __worker(self):
        while True:
            email_data = self.email_queue.get()
            if email_data is None:
                break
            send_email(email_data)
            self.email_queue.task_done()

email_queue = EmailQueue()
```