class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError
        if len(nums) == 1:
            return nums[0]

        while nums:
            n = nums.pop()
            if n not in nums:
                return n
            else:
                nums.remove(n)


    def singleNumber(self, nums: List[int]) -> int:
        from operator import xor
        from functools import reduce
        """HOLY SHIT 这个解法太神奇了, 一个数和同一个数异或两次, 得到它自身"""
        return reduce(xor, nums)