import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1


    def dequeue(self):
        # if self.size > 0:
        #     self.size -= 1
        #     print(self.storage.pop(0))
        #     return self.storage.pop(0)
        if self.storage:
            self.size -= 1
            return self.storage.pop(0)

    def len(self):
        return self.size


