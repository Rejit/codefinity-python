"""
Given two integers x and y, return a list of integers: the first being the minimum of x and y, and the second being the maximum of x and y.

"""
from typing import List

class Solution(object):
    def solve(self,x:int,y:int)->List[int]:
        print(f"x: {x}, y: {y}")
        if x > y:
            return [y, x]
        return [x, y]
