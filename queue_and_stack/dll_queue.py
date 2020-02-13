import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Because it allows us to sequentially store list elements in order to enact first in first out behavior
        self.storage = DoublyLinkedList()


    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        removed_node = self.storage.remove_from_head()
        if removed_node:
            self.size -= 1
        return removed_node

    def len(self):
        return self.size
