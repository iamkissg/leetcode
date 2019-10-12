class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [None for _ in range(k)]
        self.capacity = k
        self.head = None
        self.tail = None
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head, self.tail = 0, 0
            self.queue[self.tail] = value
            return True
        else:
            self.tail = (self.tail+1) % self.capacity
            self.queue[self.tail] = value
            return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.queue[self.head] = None

            if all(item is None for item in self.queue):
                self.head, self.tail = None, None
            else:
                self.head = (self.head+1) % self.capacity
            return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.queue[self.head] if not self.isEmpty() else -1
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.queue[self.tail] if not self.isEmpty() else -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head is None
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        # full
        if self.head is None:
            return False
        return (self.tail+1)%self.capacity == self.head%self.capacity

        


# Your MyCircularQueue object will be instantiated and called as such:
opts = ["MyCircularQueue","enQueue","enQueue","Front","enQueue","Rear","Front","Rear","Rear","Front","Front","deQueue","Front","Rear","enQueue","deQueue","deQueue","enQueue","Rear","enQueue","enQueue","enQueue","enQueue","Front","Front","enQueue","Front","Rear","Rear","Front","isFull","Rear","deQueue","enQueue","Rear","Rear","enQueue","Rear","Front","Rear","enQueue","Front","Front","enQueue","Rear","enQueue","Front","enQueue","enQueue","Rear","isFull","enQueue","enQueue","enQueue","deQueue","Rear","enQueue","Rear","deQueue","enQueue","Front","Rear","enQueue","Front","Rear","deQueue","deQueue","deQueue","enQueue","Rear","enQueue","Rear","Rear","deQueue","Front","enQueue","Front","Front","Rear","Rear","enQueue","Front","enQueue","Rear","enQueue","deQueue","Rear","enQueue","Rear","enQueue","Front","Rear","Front","Front","isFull","Front","enQueue","deQueue","Front","Rear","Rear","Front"]
vals = [[73],[52],[71],[],[1],[],[],[],[],[],[],[],[],[],[0],[],[],[0],[],[70],[45],[5],[20],[],[],[84],[],[],[],[],[],[],[],[83],[],[],[50],[],[],[],[91],[],[],[68],[],[58],[],[92],[26],[],[],[83],[37],[44],[],[],[58],[],[],[58],[],[],[49],[],[],[],[],[],[42],[],[95],[],[],[],[],[45],[],[],[],[],[55],[],[31],[],[47],[],[],[54],[],[45],[],[],[],[],[],[],[73],[],[],[],[],[]]
obj = MyCircularQueue(vals[0][0])
for opt, val in zip(opts[1:], vals[1:]):
    print(opt, val)
    if opt == 'enQueue':
        print(obj.enQueue(val[0]))
    if opt == 'deQueue':
        print(obj.deQueue())
    if opt == 'Rear':
        print(obj.Rear())
    if opt == 'Front':
        print(obj.Front())
    if opt == 'isEmpty':
        print(obj.isEmpty())
    if opt == 'isFull':
        print(obj.isFull())
    print(obj.queue)