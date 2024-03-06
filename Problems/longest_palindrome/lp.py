'''
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with 
those letters.

Letters are case sensitive, for example, "Aa" is not considered a 
palindrome here.
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        single = False
        letters = {}

        for char in s:
            if char not in letters:
                letters[char] = 1
            else: 
                letters[char] += 1

        for letter,amount in letters.items():
            if amount % 2 == 0: 
                length += amount
            else:
                if single == False:
                    length += amount
                    single = True
                else:
                    length += (amount - 1)
           
        return length
    
# Runtime: 43 ms -- beats 17.95% of users with Python3 :(
# Memory: 16.62 mb -- beats 54.93% of users with Python3