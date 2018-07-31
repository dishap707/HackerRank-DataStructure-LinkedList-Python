# -*- coding: utf-8 -*-


"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    
    p = head
    if head == None:
        return 0;
    while(p.next != None):
        p = p.next
    while(p != head):
        print(p.data)
        q = head
        while(q.next != p):
            q = q.next
        p = q 
    print(head.data) 
