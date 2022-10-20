###          ESTRUCTURA DE DATOS          ###
### Nombre: Johana Duchi Tipan            ###
### Fecha : 16/10/2022                    ###
### Tema  : DEBER 2                       ###
### Ejercicio 3: Queue using stacks       ###

#Implemente la clase Queue usando pilas- Stacks

import ctypes
class Queue(object):
    """
    Implementation of the queue data structure
    """

    def __init__(self):
        #
        self.s1 = []
        self.s2 = []
          
    def _create_queue(self, n):
        """
        Creates a new stack of capacity n
        """
        return (n * ctypes.py_object)()

class Queue(Queue):
    def enqueue(self, item):
        """
        Add new item to the queue
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        self.queue[self.l] = item
        self.l += 1

    def dequeue(self):
        """
        Remove an element from the queue
        """
        c = self.queue[0]
        for i in range(1,self.l):
            self.queue[i-1] = self.queue[i]
        self.queue[self.l - 1] = ctypes.py_object
        self.l -= 1
        return c
    
    def first(self):
        """
        Show the first element of the queue
        """
        return self.queue[0]
    
    def full(self):
        """
        Is the queue full?
        """
        if self.l == self.n:
            return True
        return False

    def empty(self):
        """
        Is the queue empty?
        """
        if self.l == 0:
            return True
        return False

    def size(self):
        """
        Return size of the queue
        """
        return self.l