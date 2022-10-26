###          ESTRUCTURA DE DATOS          ###
### Nombre: Johana Duchi Tipan            ###
### Fecha : 25/10/2022                    ###
### Tema  : DEBER 2                       ###
### Ejercicio 2: Reverse the linked list  ###

#Escriba una parte del método de la clase de lista enlazada - linked list class
#que invertirá la lista enlazada - reverse linked list. Su implementacion debe 
#visitar cada nodo en la lista solo una vez y debe usar O(1) memoria adicional.

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

        
class Linked_list:
    """
    Funcion que inicializa la cabeza de la lista enlazada -linked list
    """
    def __init__(self, head_node=None):
        self.head_node = head_node

"Clase que contiene los metodos de la singly linked list"
class Linked_list(Linked_list):          
    """
    Funcion que recorre la lista enlazada - linked list
    """
    def list_traversed(self):
        node = self.head_node
        while node:
            print(node.val,"->" , end = " ")
            node = node.next_node
    
    """
    Funcion que invierte la lista enlazada -linked list
    """
    def list_reverse(self):
        prev = None
        node = self.head_node     
        #Si la cabeza esta vacia o no hay un nodo con el que intercambiar
        if not self.head_node or not self.head_node.next_node:
            return self.head_node
        else:
            #Se atraviesa la lista
            while node:  
                # A-> B-> C-> D-> E->null
                next_node= node.next_node
                node.next_node = prev
                # E nueva head node
                prev = node 
                # E-> D->...
                node = next_node
                
        self.head_node =prev
        

m1 = Node("Jan")
m2 = Node("Feb")
m3 = Node("March")
m4 = Node("Dec")

m1.set_next_node(m2)
m2.set_next_node(m3)
m3.set_next_node(m4)

list1 = Linked_list(m1)

print ("\nLinked list: ")
list1.list_traversed()
print ("\nLinked list reverse:")
list1.list_reverse()
list1.list_traversed()