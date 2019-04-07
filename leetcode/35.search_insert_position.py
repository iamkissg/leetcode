from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            if nums[0] >= target:
                return 0
            else:
                return 1
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)
        
        spos = 0
        epos = len(nums) - 1
        mpos = spos
        while spos + 1 < epos:
            if nums[mpos] < target:
                spos = mpos
            elif nums[mpos] == target:
                return mpos
            elif nums[mpos] > target:
                epos = mpos
            mpos = (spos + epos) // 2
        else:
            return spos+1 if nums[spos] < target else spos


if __name__ == "__main__":
    sol = Solution()
    # print(sol.searchInsert([1,3,5,6], 5))
    # print(sol.searchInsert([1,3,5,6], 1))
    # print(sol.searchInsert([1,3,5,6], 2))
    # print(sol.searchInsert([1,3,5,6], 7))
    # print(sol.searchInsert([1,3,5,6], 0))
    # print(sol.searchInsert([], 0))
    # print(sol.searchInsert([1], 0))
    print(sol.searchInsert([1, 3], 1))
            