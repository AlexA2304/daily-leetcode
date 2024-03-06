class Solution:
    # boyer moore voting algorithm
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else: 
                count -= 1
        return candidate
    
# Runtime: 158 ms -- beats 25.63% of users with Python3
# Memory: 17.99 mb -- beats 80.82% of users with Python3