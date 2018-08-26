"""
Queue
"""


class Queue:
    def __init__(self):
        self._container = []
        self._head = -1

    def is_empty(self):
        return self._head == -1

    def peek(self):
        if is_empty():
            raise Exception("Access to empty queue")
        return self._container[]

    def enqueue(self, value):
        self._container.append(value)
        self._head += 1

    def dequeue(self):
        if is_empty():
            raise Exception("Access to empty queue")
        self._head -= 1
        return self._container.pop()

    def __str__(self):
        return "queue: " + str(self._container)

    def __len__(self):
        return self._head + 1
