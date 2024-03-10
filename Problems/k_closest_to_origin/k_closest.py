'''
Given an array of points where points[i] = [xi, yi] represents a point
on the X-Y plane and an integer k, return the k closest points to the 
origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean 
distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be 
unique (except for the order that it is in).
'''

import math
import numpy as np
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def square(point:List[int]) -> int:
            return math.sqrt((point[0] ** 2) + (point[1] ** 2))
        points = sorted(points, key=square)
        return points[:k]
    
# Runtime: 615 ms -- beats 36.94% of users with Python3
# Memory: 42.12 mb -- beats 5.25% of users with Python3 :(