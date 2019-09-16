class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # 输出栈非空, 则直接从输出栈 pop
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

        val = self.output_stack.pop()
        return val

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.input_stack and not self.output_stack
        


if __name__ == "__main__":
    
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_3 = obj.peek()
    print(param_3)
    obj.pop()
    obj.push(3)
    print(obj.peek())
    param_2 = obj.pop()
    param_4 = obj.empty()