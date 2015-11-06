# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:21:11 2015

@author: MS
"""
import sys

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        #" A  B C D E F G H"
        #"-2 -2 2 2 3 3 4 4"
        
        if A <= E:
            width_left = E
        else:
            width_left = A
            
        if C <= G:
            width_right = C
        else:
            width_right = G
        
        if width_left <= width_right:
            width = width_right - width_left
        else:
            width = 0 
            
        # Intersection height computation    
        if D <= H:
            height_top = D
        else:
            height_top = H
            
        if B <= F:
            height_bot = F
        else:
            height_bot = B
 
        if height_top >= height_bot:
            height = height_top - height_bot
        else:
            height = 0
        
        inter = width * height
        print inter
        area1 = (D-B)*(C-A)
        print area1
        area2 = (H-F)*(G-E)
        print area2
        
        return area1 + area2 - inter
        
if __name__ == '__main__':
    args = map(int, sys.argv[1:])
    print type(args[2])
    sol = Solution()
    area = sol.computeArea(*args)
    print area
    