

"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    if headA == None:
        return headB
    if headB == None:
        return headA
    curr = None
    if headA.data > headB.data:
        curr = headB
        headB = headB.next
    else: 
        curr = headA
        headA = headA.next
    node = curr
    while headA != None and headB != None:
        if headA.data < headB.data:
            node.next = headA
            headA = headA.next
        else:
            node.next = headB
            headB = headB.next
        node = node.next    
            
    if headA == None:
        node.next = headB
    else:
        node.next = headA
    return curr
