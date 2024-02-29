'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []
        openB = ["(", "[", "{"]
        closeB = [")", "]", "}"]

        for bracket in s:
            if bracket in openB:
                stack.append(bracket)
            else: 
                if not stack:
                    return False
                elif bracket == closeB[0]:
                    if stack[-1] != openB[0]:
                        return False
                    else:
                        stack.pop()
                elif bracket == closeB[1]:
                    if stack[-1] != openB[1]:
                        return False
                    else:
                        stack.pop()
                elif bracket == closeB[2]:
                    if stack[-1] != openB[2]:
                        return False
                    else:
                        stack.pop()
        if len(stack) != 0:
            return False
        else: 
            return True
    
# Runtime: 39 ms -- Beats 34.71% of users with Python 3
# Memory: 16.49 mb -- Beats 98.84% of users with Python 3