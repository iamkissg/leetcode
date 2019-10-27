class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        '''
        20191023

        96 ms	16.6 MB	Python3
        双指针滑动窗口
        '''
        if not nums:
            return 0
        if sum(nums) < s:
            return 0
        
        n = len(nums)
        l = 0
        t = nums[l]
        if t >= s:
            return 1

        min_len = n
        for r in range(1, n):
            t += nums[r]

            while t >= s:
                if r-l < min_len:
                    min_len = r-l+1
                t -= nums[l]
                l += 1
        return min_len