from typing import List
import heapq
import bisect

class Solution:
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     '''
    #     20191005
    #     316 ms	19.9 MB	Python3
    #     这肯定不是面试官想要的解法.
    #     '''
    #     nums = []
    #     for row in matrix:
    #         nums.extend((row))
    #     nums.sort()
    #     return nums[k-1]

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''
        20191005

        220 ms	19.7 MB	Python3
        Youtube 上看到的采用二分查找的方式来, 有些神奇的
        '''
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n-1][n-1]
        while lo <= hi:
            mid = (lo+hi) // 2
            # 查找插入的位置, 如果 mid 在某一行的插入位置是 0, 说明它比这一行所有的数都小, 通过求和可以确定有多少个数排在 mid 之前
            pos = sum(bisect.bisect_right(row, mid) for row in matrix)

            if pos < k:
                lo = mid + 1
            elif pos > k:
                hi = mid - 1
            else:
                break

        return lo


    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     '''
    #     20191005
    #     252 ms	19.7 MB	Python3

    #     最小堆的做法比排序要快
    #     '''
    #     n = len(matrix)
    #     if k == 1:
    #         return matrix[0][0]
    #     elif k == n*n:
    #         return matrix[-1][-1]

    #     nums = []
    #     capacity = n*n + 1 - k
    #     heapq.heapify(nums)
    #     for row in matrix:
    #         for item in row:
    #             if not nums:
    #                 heapq.heappush(nums, item)
    #                 capacity -= 1
    #             elif item > nums[0]:
    #                 if capacity:
    #                     heapq.heappush(nums, item)
    #                     capacity -= 1
    #                 else:
    #                     heapq.heapreplace(nums, item)
    #     return nums[0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.kthSmallest(matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,))
    print(sol.kthSmallest(matrix = [
   [1], 
],
k = 1,))