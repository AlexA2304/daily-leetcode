'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct 
ways can you climb to the top?
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        return self.helper(n, 1, 2)
        
    def helper(self, n, secondLast, last):
        if n == 2:
            return last
        
        current = secondLast + last

        return self.helper(n - 1, last, current)
    
# Runtime: 38 ms -- beats 34.05% of users with Python3
# Memory: 16.40 mb -- beats 92.66% of users with Python3