from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        if val not in nums:
            return len(nums)
        
        pos = 0
        while True:
            if pos == len(nums) or not len(nums):
                break
            if nums[pos] == val:
                del nums[pos]
            else:
                pos += 1
        return len(nums)


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeElement([3,2,2,3], 2))
    print(sol.removeElement([], 2))
    print(sol.removeElement([1], 2))
    print(sol.removeElement([2], 2))
    print(sol.removeElement([2, 2], 2))
    print(sol.removeElement([0,1,2,2,3,0,4,2], 2))