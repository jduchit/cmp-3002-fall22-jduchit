### Nombre: Johana Duchi Tipan            ###
### Fecha : 20/10/2022                    ###
### Tema  : Extra Points                  ###
### EP: Deep copy of a linked list        ###

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

class Singly_linked_list(Singly_linked_list):
    
    def insert_end(self, val):
        node = self.head_node        
        while node.next_node:
            node = node.next_node           
        new_node = Node(val)
        node.next_node = new_node
        
    def list_traversed(self):
        node = self.head_node
        while node:
            print(node.val,"->" , end = " ")
            node = node.next_node

def swap(head_node):
    
    # Base
    # In head is none or we don't have a node to swap with
    if not head_node or not head_node.next_node:
        return head_node
    
    # Nodes to be swapped
    first = head_node
    second = head_node.next_node
    
    # Call the function with the reduce scope and recursion
    first.next_node  = swap(second.next_node)
    second.next_node = first

    # What do we return? (New head)
    # Now the head is the second node
    return second
    
def deepCopy(head_node):  
    # In head is none or we don't have a node to deepCopy with
    if not head_node or not head_node.next_node:
        return head_node
    else:  
        node = Node(head_node.val)
        node.next_node =deepCopy(head_node.next_node)
    return node   

a = Node('A')
L = Singly_linked_list(a)
L.insert_end('B')
L.insert_end('C')
L.insert_end('D')
L.insert_end('E')
L.insert_end('F')
L.insert_end('G')
L.insert_end('H')
L.insert_end('I')
L.insert_end('J')


print("\nOriginal linked list L: ")
L.list_traversed()

print("\nDeep Copy of the linked list use swap L1: ")
L1 = deepCopy(L.head_node)
L1 = swap(L.head_node)
L1 = Singly_linked_list(L1)
L1.list_traversed()

print("\nDeep Copy of the linked list L2: ")
L2 = deepCopy(L.head_node)
L2 = Singly_linked_list(L2)
L2.head_node.next_node = None
L2.list_traversed()

print("\nOriginal linked list L: ")
L.list_traversed()
