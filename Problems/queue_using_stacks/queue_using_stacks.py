'''
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal 
queue (push, peek, pop, and empty).

Implement the MyQueue class:

- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push to top, 
peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may 
simulate a stack using a list or deque (double-ended queue) as long as you 
use only a stack's standard operations.
'''

class MyQueue:

    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def push(self, x: int) -> None:
        self.stackIn.append(x)

    def pop(self) -> int:
        if not self.stackOut:
            self.reverse()
        return self.stackOut.pop()

    def peek(self) -> int:
        if not self.stackOut:
            self.reverse()
        return self.stackOut[-1]

    def empty(self) -> bool:
        return not self.stackIn and not self.stackOut
    
    def reverse(self) -> None:
        for i in reversed(range(len(self.stackIn))):
                self.stackOut.append(self.stackIn[i])
        self.stackIn.clear()
            


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
        
# Runtime: 34 ms -- beats 63.22% of users with Python3
# Memory: 16.65 mb -- beats 25.71% of users with Python3