import bisect


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.left = None
        self.right = None

    def addNum(self, num: int) -> None:
        if not self.nums:
            self.left, self.right = 0, 0
        else:
            if self.left == self.right:
                self.right += 1
            else:
                self.left += 1
        bisect.insort_left(self.nums, num)

    def findMedian(self) -> float:
        if not self.nums:
            raise Exception()

        return (self.nums[self.left]+self.nums[self.right])/2


if __name__ == "__main__":
    ["addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
    [[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]
    obj = MedianFinder()
    obj.addNum(6)
    print(obj.findMedian())
    obj.addNum(10)
    print(obj.findMedian())
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(6)
    print(obj.findMedian())
    obj.addNum(5)
    print(obj.findMedian())
    obj.addNum(0)
    print(obj.findMedian())
    obj.addNum(6)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
    obj.addNum(1)
    print(obj.findMedian())
    obj.addNum(0)
    print(obj.findMedian())
    obj.addNum(0)
    print(obj.findMedian())

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()