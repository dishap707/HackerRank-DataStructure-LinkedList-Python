

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
    A =headA
    B= headB
    countA= 0
    countB = 0
    while A.next!= None:
        A = A.next
        countA =countA+ 1
    while B.next != None:
        B = B.next
        countB = countB +  1
    if countA != countB:
        return 0
    
    while A.next != None or B.next != None:
        if A.data != B.data:
            return 0
        A = A.next
        B = B.next
    if A.data != B.data:
        return 0
    return 1