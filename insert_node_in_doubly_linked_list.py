#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    temp = head 
    new_node = DoublyLinkedListNode(data)
    
    # Starting Position 
    if new_node.data < temp.data:
        new_node.next = head
        head.prev = new_node
        return new_node

    # Reaching Position at which the node is to be added
    temp = head
    next_temp = head.next
    while((next_temp != None) and (new_node.data > next_temp.data)):
        temp = next_temp
        next_temp = next_temp.next
    
    
    if next_temp == None:
        # End position insertion
        temp.next = new_node
        new_node.prev = temp
    else:
        # Middle Position insertion
        temp.next = new_node
        next_temp.prev = new_node
        new_node.prev = temp
        new_node.next = next_temp
          
    return head

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
