class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_stack) == 0 or x < self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])
        
    def pop(self) -> None:
        if len(self.min_stack) > 0:
            self.min_stack.pop()
            return self.stack.pop()
        else:
            raise Exception('Pop from empty stack')

    def top(self) -> int:
        if len(self.min_stack) > 0:
            return self.stack[-1]
        else:
            raise Exception('Empty stack has no items.')

    def getMin(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        else:
            raise Exception('Empty stack has no items.')


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()