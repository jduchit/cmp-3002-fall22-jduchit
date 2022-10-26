###          ESTRUCTURA DE DATOS          ###
### Nombre: Johana Duchi Tipan            ###
### Fecha : 16/10/2022                    ###
### Tema  : DEBER 2                       ###
### Ejercicio 1: Singly linked lists      ###

#Implemente la clase Stacks y todos sus métodos usando listas enlazadas 
#simples - singly linked lists. Analizar el tiempo de ejecución y 
#la complejidad de la memoria, y comparar con lo que estudiamos en clase
import ctypes
import time

"""
La funcion medidor_tiempo se encarga de medir el tiempo de ejecucion de un programa.
"""
def medidor_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()*10**6
        c = funcion(*args, **kwargs)
        fin = time.time()*10**6
        #Se resta el segundo que puse en el sleep
        print("La funcion analizada es: ",funcion.__name__,
              " , el tiempo que se demora el programa en ejecutarse es: {} micro segundos"
              .format((fin - inicio)-(10**6)))
        return c
    return funcion_medida

"""
Clase que crea los nodos de la linked list
"""
class Node:
    """
    Implementation of a node
    """
    def __init__(self, val=None):
        self.val = val
        self.next_node = None
    
    def set_next_node(self, next_node):
        self.next_node = next_node

class Stack(object):
    """
    Funcion que inicializa la cabeza de la lista enlazada
    """
    def __init__(self, n,head_node=None):
        self.head_node = head_node
        self.count_node =0
        self.n= n
        self.stack = self._create_stack(self.n)       
    
    def _create_stack(self, n):
        """
        Creates a new stack of capacity n
        """
        return (n * ctypes.py_object)()
    
"""
Clase que crea el stack usando el principio LIFO lo ultimo en entrar es
lo primero en salir
"""    
class Stack(Stack):   
    """
    Funcion que almacena un elemento en el stack
    """
    @medidor_tiempo
    def push(self, new_node):
        time.sleep(1)
        if self.n == self.size():
            raise ValueError("no more capacity")
        else:
            if self.head_node is None:
                self.head_node = Node(new_node)
            else:
                new_node = Node(new_node)
                new_node.next_node = self.head_node
                self.head_node = new_node
        #Suma los elementos que se van a
        self.count_node+=1
        
    """
    Funcion que elimina el primer elemento de la pila
    """
    @medidor_tiempo
    def pop(self):
        time.sleep(1)
        """
        Verificamos si el stack esta vacio, usando la funcion empty
        """
        if self.empty():
            return None
        else:
            prev = self.head_node
            self.head_node = prev.next_node
            #Borramos el puntero
            prev.next_node =None
        self.count_node-=1
    
    """
    Funcion que retorna la cabeza del stack
    """
    @medidor_tiempo
    def top(self):
        time.sleep(1)
        """
        Verificamos si el stack esta vacio, usando la funcion empty
        """
        if self.empty():
            return None
        else:            
            return self.head_node.val
        
    
    """
    Funcion que verifica si el stack esta lleno
    """ 
    @medidor_tiempo
    def full(self):
        time.sleep(1)
        return self.n == self.size()
        
        # if self.l == self.n:
        #    return True
        # return False
        
    """
    Funcion que verifica si esta lleno el stack
    """
    @medidor_tiempo
    def empty(self):
        time.sleep(1)
        return self.head_node==None
        #if self.head_node == 0:
        #    return True
        #else:
        #    return False

    """
    Funcion que retorna el tamanio del stack
    """
    @medidor_tiempo
    def size(self):
        time.sleep(1)
        return self.count_node
    
    @medidor_tiempo
    def stack_traversed(self):
        time.sleep(1)
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node
    
S = Stack(3)
S.push(1)
S.push(2)
S.push(4)

print("-----------------------------------------------------------")
print("The stack is:")
S.stack_traversed()
print("The stack is full: ",S.full())
print("The size of stack is: ",S.size())
S.pop()
print("The new stack after method pop is:")
S.stack_traversed()
print("The stack top is :",S.top() )
print("The stack is full: ",S.full())
print("The stack is empty: ", S.empty())
print("The size of stack is: ",S.size())
 

    