'''
Given two strings s and t, return true if t is an anagram 
of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging 
the letters of a different word or phrase, typically using 
all the original letters exactly once.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        CharsInS = {}
        for char in s:
            if char in CharsInS:
                CharsInS[char] += 1
            else: 
                CharsInS[char] = 1

        for char in t:
            if char in CharsInS and CharsInS[char] >= 1:
                CharsInS[char] -= 1
                if CharsInS[char] == 0:
                    CharsInS.pop(char)
            else:
                return False

        return True
    
# Runtime: 47 ms -- beats 69.84% of users with Python3
# Memory: 17.76 mb -- beats 76.66% of users with Python3