"""
Bear Bill wants to become the largest of bears, or at least to become larger than his brother Bob. Right now, Bill and Bob weigh a and b respectively. It's guaranteed that Bill's weight is smaller than or equal to his brother's weight. Bill eats a lot and his weight is tripled after every year, while Bob's weight is doubled after every year. After how many full years will Bill become strictly heavier than Bob?

Example 1
Input:
a = 4; b = 7
Output:
2
"""

class Solution(object):
    def solve(self,bill,bob):
        print(f"a: {bill}, b: {bob}")
        times = 0
        
        while (bill <= bob):
            bill *= 3
            bob *= 2
            times += 1
        
        return times