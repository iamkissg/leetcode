from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        20191016

        经网友提醒, 维护两个数组, 分别保存当前位置左边的连乘结果, 右边的连乘结果, 于是要求的当前位置的值就是左右元素的值
        '''

        if not nums:
            return []
        
        n = len(nums)
        left = [1]+[nums[0] for _ in range(n-1)]
        right = [nums[-1] for _ in range(n-1)] + [1]
        for i in range(2, n):
            left[i] = left[i-1] * nums[i-1]
        for i in range(n-3, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        # print(left)
        # print(right)
        
        res = [None for _ in range(n)]
        for i in range(n):
            res[i] = left[i] * right[i]

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))
