class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        20191021
        68 ms	13.9 MB	Python3
        '''
        if not nums:
            return 0
        
        i = 2
        while i < len(nums):
            if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)