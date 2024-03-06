'''
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with 
those letters.

Letters are case sensitive, for example, "Aa" is not considered a 
palindrome here.
'''

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        letters = Counter(s)

        for letter,amount in letters.items():
            length += amount // 2 * 2

        if len(s) > length:
            length += 1
           
        return length
    
# Runtime: 29 ms -- beats 94.29% of users with Python3 :)
# Memory: 16.59 mb -- beats 90.85% of users with Python3