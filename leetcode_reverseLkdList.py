# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:12:59 2015
@author: MkSavvy

This file is a leetcode solution for the reversal of a linked List
the reverseLL() method receives a Linked list 'pointer' with which to
work with, must return a point to a reversed version of the list

Issues: ...
"""
import sys

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        

class Solution(object):
    
    def reverseLL(self, head):
        
        cur = head  # pointer to the current node to look at
        
        # we take the cur.next node and send it to beginning at head
        while cur.next != None:
            anchor = head
            head = cur.next
            cur.next = cur.next.next
            head.next = anchor
            
        return head
            
            
if __name__ == "__main__":
    
    fakehead = ListNode(None)
    
    # fill the linked list
    last = fakehead
    args = list(sys.argv[1])    
    
    for c in args[:]:
        last.next = ListNode(c)
        last = last.next
    
    # check the Solution
    sol = Solution()
    revList = sol.reverseLL(fakehead.next)
    
    cur = revList
    while cur != None:
        print cur.val
        cur = cur.next
    