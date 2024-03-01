'''
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters 
and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        pal = re.sub(r'\W+', '', s).lower()
        pal = re.sub('_', '', pal)

        left = 0
        right = len(pal) - 1

        while left < right:

            if pal[left] != pal[right]:
                return False
            
            left += 1
            right -= 1

        return True
    
# Runtime: 48 ms -- Beats 42.72% of users with Python 3
# Memory: 17.87 mb -- Beats 37.89% of users with Python 3