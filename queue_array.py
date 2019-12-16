#
#Name: Nicholas Wachter
#Student ID: 016170774
#Date (last modified): 4/18/19
#
# Lab 11
# Section 12
# Purpose of Lab: to write my own queue data type using an array

class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity=5):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0
        self.front = 0
        self.end = 0

    def peek(self):
        return self.items[self.front]

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        if self.num_items == 0:
            return True
        return False


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        if self.num_items == self.capacity:
            return True
        return False


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.num_items == self.capacity:
            raise IndexError
        self.items[self.end] = item
        self.end = (self.end+1)%self.capacity
        self.num_items += 1

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.num_items == 0:
            raise IndexError
        returnItem = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1)%self.capacity
        self.num_items -= 1
        return returnItem

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items

