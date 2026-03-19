"""
Bill studies in a school and he adores Maths. His class has been studying arithmetic expressions. On the last class the teacher wrote three positive integers a, b, c on the blackboard. The task was to insert signs of operations + and *, and probably brackets between the numbers so that the value of the resulting expression is as large as possible.

Possible variants:

a+b*c=v1
a*(b+c)=v2
a*b*c=v3
(a+b)*c=v4
Note that you can insert operation signs only between a and b, and between b and c, that is, you cannot swap integers. For instance, in the given sample you cannot get expression (a+c)*b.

Given an integers a, b and c. Return maximum value of the expression that you can obtain.

Example 1
Input:
a = 1, b = 2, c = 3
Output:
9
"""

class Solution(object):
    def solve(self,a:int,b:int,c:int)->int:
        print(f"a: {a}, b: {b}, c: {c}")
        v1 = a + b * c
        v2 = a * (b + c)
        v3 = a * b * c
        v4 = (a + b) * c
        return max(v1, v2, v3, v4)
