"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Reverse(head):
    if head is None:
        return None
    prev = None
    curr = head
    aux = head.next
    while curr is not None:
        curr.next = prev
        prev = curr
        curr = aux
        if curr is not None:
            aux = aux.next
    return prev

