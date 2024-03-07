'''
Given two binary strings a and b,
return their sum as a binary string.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""

        pointerA = len(a) - 1
        pointerB = len(b) - 1

        while pointerA >= 0 or pointerB >= 0 or carry > 0:

            if pointerA >= 0:
                carry += int(a[pointerA])
                pointerA -= 1
            if pointerB >= 0:
                carry += int(b[pointerB])
                pointerB -= 1

            resultBit = carry % 2
            carry = carry // 2

            result += str(resultBit)
        return result[::-1]
    
# Runtime: 37 ms -- beats 61.21% of users with Python3
# Memory: 16.60 mb -- beats 78.23% of users with Python3