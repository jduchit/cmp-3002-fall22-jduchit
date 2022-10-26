###          ESTRUCTURA DE DATOS          ###
### Nombre: Johana Duchi Tipan            ###
### Fecha : 25/10/2022                    ###
### Tema  : DEBER 2                       ###
### Ejercicio 5: Suma de numeros con singly linked list ###

class Node:
    """
    Implementation of a node
    """
    def __init__(self, val=None):
        self.val = val
        self.next_node = None
    
    def set_next_node(self, next_node):
        self.next_node = next_node
        
class Singly_linked_list:
    """
    Implementation of a singly linked list
    """
    def __init__(self, head_node=None):
        self.head_node = head_node
        
    def list_traversed(self):
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node

"Clase que contiene los metodos de la singly linked list"
class Singly_linked_list(Singly_linked_list):
    
    def insert_tail(self, new_node):
        if self.head_node:
            node = self.head_node
            while node.next_node:
                node =node.next_node
            node.next_node = new_node
        else:
            self.head_node = new_node
            
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
    
"""
Funcion que transforma numero a singly linked
"""
def num_to_list(num):
    lista=Singly_linked_list()
    for i in str(num):
        lista.insert_tail(Node(int(i)))
    return lista  

"""
Funcion que suma las listas
"""
def sum_list(list1,list2,list3):
    #Para suma se revierte la lista para poder hacer unidades,decenas,etc
    list1.list_reverse()
    list2.list_reverse()
    list3.list_reverse()
    
    suma_lista = Singly_linked_list
    num_llevando = 0
    
    temp_suma = list1.head_node.val+list2.head_node.val+list3.head_node.val+num_llevando
    if (temp_suma>10):
        suma_lista.head_node=(temp_suma-10)
        num_llevando=1
        
        suma_lista.list_traversed()
        return suma_lista
   
print("\n Linked list 1: ")   
list1=num_to_list(345)
list1.list_traversed()
print("\n Linked list 2: ") 
list2=num_to_list(289)
list2.list_traversed()
print("\n Linked list 3: ") 
list3=num_to_list(716)
list3.list_traversed()
print("\n Suma total: ") 
list4 = sum_list(list1,list2,list3)
