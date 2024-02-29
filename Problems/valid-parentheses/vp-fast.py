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
        if len(s) % 2 != 0:
            return False

        brackets = {")":"(", "]":"[", "}":"{"}
        stack = []

        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            elif stack and stack[-1] == brackets.get(bracket):
                stack.pop()
            else:
                return False

        return not stack
    
# Runtime: 31 ms -- Beats 83.42% of users with Python 3
# Memory: 16.66 mb -- Beats 49.54% of users with Python 3