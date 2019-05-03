class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> None:
        if not self.stack:
            raise RuntimeError('Pop from empty stack')
        self.stack.pop()
        

    def top(self) -> int:
        if not self.stack:
            raise RuntimeError('Top from empty stack')
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.stack:
            raise RuntimeError('getMin from empty stack')
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()