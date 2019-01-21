"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head == None:
        return False
    
    # Classic floyd's cycle detection algorithm. (slow-fast)
    # slow will cover x distance
    # fast will cover x+s distance
    # There will be a point where both of these pointers will meet which will be our starting point.
    
    # Intuitive Hash map solution
    seen = []
    while(head != None):
        seen.append(head)
        head = head.next
        if head in seen:
            return True
    
    return False
    #pass
