import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        if len(self.nums) > self.k:
            while len(self.nums) > self.k:
                heapq.heappop(self.nums)

    # NOTE: 粗糙的 heapq 操作
    # def add(self, val: int) -> int:
    #     if len(self.nums) < self.k:
    #         heapq.heappush(self.nums, val)
    #     else:
    #         min_val = heapq.heappop(self.nums)
    #         if val > min_val:
    #             heapq.heappush(self.nums, val)
    #         else:
    #             heapq.heappush(self.nums, min_val)
    #     min_val = heapq.heappop(self.nums)
    #     heapq.heappush(self.nums, min_val)
    #     return min_val


    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        else:
            if val > self.nums[0]:
                heapq.heapreplace(self.nums, val)
        return self.nums[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)