from typing import List

import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        最大堆写法
        执行用时 :1572 ms, 在所有 Python3 提交中击败了5.17% 的用户
        内存消耗 :20.1 MB, 在所有 Python3 提交中击败了5.39%的用户
        '''
        if not nums: return []
        if len(nums) <= k: return [max(nums)]

        init_nums = nums[:k]
        heapq._heapify_max(init_nums)
        result = [init_nums[0]]

        for i in range(k, len(nums)):
            # 眼看着这一段的效率就不高, 是真的慢啊
            # init_nums.remove(nums[i-k])
            # init_nums.append(nums[i])
            # heapq._heapify_max(init_nums)
            result.append(init_nums[0])
        return result

    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     '''
    #     连这个看上去很蠢的写法都比 Python 不完全的最大堆写法更好
    #     执行用时 :804 ms, 在所有 Python3 提交中击败了17.92% 的用户
    #     内存消耗 :20.2 MB, 在所有 Python3 提交中击败了5.39%的用户
    #     '''
    #     if not nums: return []
    #     if len(nums) <= k: return [max(nums)]
    #     return [max(nums[i: i+k]) for i in range(len(nums)-k+1)]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        双端队列写法, 来自覃超的算法课 (看不懂代码, 先跑一遍)
        执行用时 :216 ms, 在所有 Python3 提交中击败了75.74% 的用户
        内存消耗 :20.3 MB, 在所有 Python3 提交中击败了5.39%的用户
        '''
        if not nums: return []
        if len(nums) <= k: return [max(nums)]

      
        window = []  # window 存的是下标
        result = []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i-k:  # 右边的条件成立, 说明移动了窗口, 需要将队列头的元素删除
                window.pop(0)
            # 从后删除索引, 直到索引窗口的最后一个元素对应的数值 > x
            # 这一步保证队列的头个元素一定是窗口中最大的, 虽然理解起来挺绕的
            # 拿 -1 比较的原因是, 用 pop
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            # 达到 k 之前才考虑最大值
            if i >= k-1:
                result.append(nums[window[0]])
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))