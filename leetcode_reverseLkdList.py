# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:12:59 2015
@author: MkSavvy

This file is a leetcode solution for the reversal of a linked List
the reverseLL() method receives a Linked list 'pointer' with which to
work with, must return a point to a reversed version of the list

Issues: ...
"""

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        

class Solution(object):
    
    def reverseLL(self, head):
        
        cur = head  # pointer to the current node to look at
        while cur != None:
            anchor = head
            head = cur.next
            cur.next = cur.next.next
            head.next = anchor
            
            
            
if __name__ == "__main__":
    myLL = ListNode('a')
    string = list('string')
    
    # fill the linked list
    current = myLL
    for c in string:
        current.next = ListNode(c)
        current = current.next
    
    # check the Solution
    sol = Solution()
    revList = sol.reverseLL(myLL)
    
    cur = revList
    while cur != None:
        print cur.val
        cur = cur.next
    