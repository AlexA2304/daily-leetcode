'''
You are given an array of non-overlapping intervals intervals where
intervals[i] = [starti, endi] represent the start and the end of the ith 
interval and intervals is sorted in ascending order by starti. You are 
also given an interval newInterval = [start, end] that represents the 
start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in 
ascending order by starti and intervals still does not have any 
overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            interval = intervals[i]

            if newInterval[1] < interval[0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            elif newInterval[0] > interval[1]:
                result.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]

        result.append(newInterval)
        return result
    
# Runtime: 72 ms -- beats 76.20% of users with Python3
# Memory: 19.90 mb -- beats 82.77% of users with Python3