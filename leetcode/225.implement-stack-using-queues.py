from queue import Queue


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_1 = Queue()
        self.queue_2 = Queue()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.queue_1.qsize():
            self.queue_1.put(x)
        else:
            self.queue_2.put(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.queue_1.qsize():
            for _ in range(self.queue_2.qsize()-1):
                self.queue_1.put(self.queue_2.get())
            val = self.queue_2.get()
            return val
        else:
            for _ in range(self.queue_1.qsize()-1):
                self.queue_2.put(self.queue_1.get())
            val = self.queue_1.get()
            return val

        

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.queue_1.qsize():
            for _ in range(self.queue_2.qsize()-1):
                self.queue_1.put(self.queue_2.get())
            val = self.queue_1.get()
            self.queue_2.put(val)
            return val
        else:
            for _ in range(self.queue_1.qsize()-1):
                self.queue_2.put(self.queue_1.get())
            val = self.queue_2.get()
            self.queue_1.put(val)
            return val
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not (self.queue_1.qsize() +self.queue_2.qsize())


if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.pop()
    param_4 = obj.empty()
        