###          ESTRUCTURA DE DATOS          ###
### Nombre: Johana Duchi Tipan            ###
### Fecha : 17/11/2022                    ###
### Tema  : DEBER 3                       ###
### Ejercicio 1: Merge two sorted lists   ###

#Suponga que tiene dos listas enlazadas ordenadas. Utilice la recursividad para
#fusionar estas listas y devolver una nueva lista ordenada.

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
        
"""
clase que crea la singly linked list
"""
class Singly_linked_list:
    """
    Funcion que inicializa la cabeza de la lista enlazada -linked list
    """
    def __init__(self, head_node=None):
        self.head_node = head_node
        
    """
    Funcion que recorre la lista enlazada - linked list
    """
    def list_traversed(self):
        node = self.head_node
        while node:
            print(node.val,"->" , end = " ")
            node = node.next_node 
        print("Null")
        
    """
    Funcion que inserta al final de la linked list
    """
    def insert_tail(self, new_node):
        node = self.head_node
        prev = None
        while node:
            prev = node
            node = node.next_node
        prev.set_next_node(new_node)
    
    """
    Funcion que agrega los nodos en orden, sirve si las 2 listas estan 
    desordenadas
    """
    def insert_sorted(self,data):
      node = Node(data.val)
      curr = self.head_node
      prev = None
    
      while curr is not None and curr.val > data.val:
        prev = curr
        curr = curr.next_node
    
      if prev == None:
        self.head_node = node
      else:
        prev.next_node = node
    
      node.next_node = curr
    

"""
Funcion que ordena la lista de numeros siempre y cuando las listas que se le
entreguen esten ordenadas
"""
def merge_sort(list1,list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1
     
    if list1.val < list2.val:
        list1.next_node = merge_sort(list1.next_node, list2)
        return list1
    else:
        list2.next_node = merge_sort(list1, list2.next_node)
        return list2

#Se crea la linked list 1
list1 = Singly_linked_list(Node(2))
list1.insert_tail(Node(6))
list1.insert_tail(Node(8))
print ("List 1: ")
list1.list_traversed()

#Se crea la linked list 2
list2 = Singly_linked_list(Node(1))
list2.insert_tail(Node(3))
list2.insert_tail(Node(4))
list2.insert_tail(Node(5))
list2.insert_tail(Node(7))
print ("\n\nList 2: ")
list2.list_traversed()

#Se crea la linked list 3 que contenga el contenido de list 1 y list 2
list3 = Singly_linked_list(merge_sort(list1.head_node, list2.head_node))
print ("\n\nList 3: ")
list3.list_traversed()