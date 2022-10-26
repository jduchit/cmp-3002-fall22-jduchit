###          ESTRUCTURA DE DATOS          ###
### Nombre: Johana Duchi Tipan            ###
### Fecha : 25/10/2022                    ###
### Tema  : DEBER 2                       ###
### Ejercicio 3: Queue using stacks       ###

#Implemente la clase Queue usando pilas- Stacks

import ctypes

class Stack(object):
    """
    Implementation of the stack data structure
    """

    def __init__(self, n):
        self.l = 0
        self.n = n
        self.stack = self._create_stack(self.n)        
    
    def _create_stack(self, n):
        """
        Creates a new stack of capacity n
        """
        return (n * ctypes.py_object)()

class Stack(Stack):
    def push(self, item):
        """
        Add new item to the stack
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        self.stack[self.l] = item
        self.l += 1

    def pop(self):
        """
        Remove an element from the stack
        """
        if not self.l:
            raise('stack is empty')
        c = self.stack[self.l-1]
        self.stack[self.l] = ctypes.py_object
        self.l -= 1
        return c
    
    def empty(self):
        """
        Is the stack empty?
        """
        return self.l == 0    

    def size(self):
        """
        Return size of the stack
        """
        return self.l   
    
    def top(self):
        """
        Show the top element of the stack
        """
        return self.stack[self.l-1]
    
    def traverse(self):
       for i in range(self.l):
           print(self.stack[i])
           self.stack[i]
           i+=1
            
class Queue(object):
    def __init__(self,n):
        self.n = n
        self.s1 = Stack(n)
        self.s2 = Stack(n)

    def enqueue(self, item):
        self.s1.push(item)
        #print(item,"->" , end = " ")

    def dequeue(self):
        if self.s2.empty():
            while not self.s1.empty():
                temp= self.s1.pop()
                self.s2.push(temp)
        return self.s2.pop()
    
    """
    Show the first element of the queue
    """
    def first(self):
      if not self.s1 and not self.s2:
          #raise('Queue is empty')  
          return print ("The first item in s1 is : ", None, 
                        ", The first item in s2 is: ", None)
      elif not self.s2:
          return print ("The first item in s1 is : ", self.s1.top(), 
                        ", The first item in s2 is: ",self.s2.top())
        
    """
    Is the queue full?
    """    
    def full(self):
      return print ("Is full s1? : ", self.s1.size==self.n, ", Is full s2? : ",
                    self.s2.size==self.n)
    
    """
    Comprueba si la cola - Queue esta vacia
    """
    def empty_queue(self): 
        return print ("Is empty s1? : ", self.s1.size()==0, ", Is empty s2? : ",
                      self.s2.size()==0)
        
    """
    Retorna el size de la cola -queue
    """
    def size_queue(self):
        return print ("Size s1 : ", self.s1.size(), ", Size s2 : ",self.s2.size())
    
    
    def traverse_queue(self):
        print("s1: ")
        print(self.s1.traverse())
        print("s2: ")
        print(self.s2.traverse())
    
q = Queue(10)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.first()
q.full()
q.empty_queue()
q.size_queue()
q.traverse_queue()
print("\n")
q.dequeue()
q.first()
q.full()
q.empty_queue()
q.size_queue()
q.traverse_queue()
print("\n")
q.dequeue()
q.first()
q.full()
q.empty_queue()
q.size_queue()
q.traverse_queue()
print("\n")
q.dequeue()
q.first()
q.full()
q.empty_queue()
q.size_queue()
q.traverse_queue()
