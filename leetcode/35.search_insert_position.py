from typing import List
import bisect


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

    def searchInsert_bisect(self, nums: List[int], target: int) -> int:
        '''
        20191007
        bisect 一行代码搞定
        # 52 ms	14.4 MB
        '''
        return bisect.bisect_left(nums, target)

    def searchInsert_binary_search(self, nums: List[int], target: int) -> int:
        '''
        20191007
        64 ms	14.1 MB	Python3

        二分查找法, 值相同时, 在左边插入, 因此问题转换成了寻找左边界的问题,
        '''
        if not nums:
            return 0

        n = len(nums)

        l, r = 0, n  # 左闭右开, 以便 target > num[-1] 时, 能在 nums 末尾插入
        while l < r:
            mid = l+(r-l)//2

            if nums[mid] == target:
                r = mid
            elif nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid
        return l


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert_bisect([1,3,5,6], 7))
    print(sol.searchInsert_bisect([1,3,5,6], 5))
    print(sol.searchInsert_bisect([1,3,5,6], 1))
    print(sol.searchInsert_bisect([1,3,5,6], 2))
    print(sol.searchInsert_bisect([1,3,5,6], 0))
    print(sol.searchInsert_bisect([], 0))
    print(sol.searchInsert_bisect([1], 0))
    print(sol.searchInsert_bisect([1, 3], 1))
    print()

    print(sol.searchInsert_binary_search([1,3,5,6], 5))
    print(sol.searchInsert_binary_search([1,3,5,6], 1))
    print(sol.searchInsert_binary_search([1,3,5,6], 2))
    print(sol.searchInsert_binary_search([1,3,5,6], 7))
    print(sol.searchInsert_binary_search([1,3,5,6], 0))
    print(sol.searchInsert_binary_search([], 0))
    print(sol.searchInsert_binary_search([1], 0))
    print(sol.searchInsert_binary_search([1, 3], 1))
            