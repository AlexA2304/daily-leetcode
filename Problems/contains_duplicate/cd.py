'''
Given an integer array nums, return true if any 
value appears at least twice in the array, and 
return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = set()

        for num in nums:
            if num in numbers:
                return True
            else:
                numbers.add(num)
        return False
    
# Runtime: 421 ms -- beats 54.93% of users with Python3
# Memory: 17.58 mb -- beats 70.85% of users with Python3