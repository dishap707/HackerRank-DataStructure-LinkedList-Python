# -*- coding: utf-8 -*-
"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self

def RemoveDuplicates(head).data = data
       self.next = next_node
def RemoveDuplicates(head):
    node = head
    while node.next:
        if node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next
    return head
 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
 
    node = head
    while node.next:
        if node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next
    return head
