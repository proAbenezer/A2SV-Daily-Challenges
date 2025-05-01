# Problem: Min Stack - https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.minStack: 
            self.minStack.append([val, val])
            return
        prevMin = self.minStack[-1][1]
        if prevMin < val:
            self.minStack.append([val, prevMin])
        else: 
            self.minStack.append([val, val])
    
    def pop(self) -> None:
        self.minStack.pop()

    def top(self) -> int:
        return self.minStack[-1][0]

    def getMin(self) -> int:
        return self.minStack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()