'''
Given two strings ransomNote and magazine, return true if ransomNote can 
be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = defaultdict(int)
        for char in range(len(magazine)):
            letters[magazine[char]] += 1 
        for char in ransomNote:
            if char in letters and letters[char] > 0:
                letters[char] -= 1
            else: 
                return False
        return True
    
# Runtime: 59 ms -- beats 49.48% of users with Python3
# Memory: 16.69 mb -- beats 88.16% of users with Python3