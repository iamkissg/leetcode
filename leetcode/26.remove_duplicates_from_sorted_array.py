from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        pos = 0
        while True:
            if len(nums) == 1:
                return 1
            if pos == len(nums) - 1:
                break
            if nums[pos] == nums[pos+1]:
                del nums[pos+1]
                continue
            pos += 1
        return len(nums)


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1,1,2]))
    print(sol.removeDuplicates([1,2,2]))
    print(sol.removeDuplicates([1,1]))
    print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(sol.removeDuplicates([0]))
    print(sol.removeDuplicates([]))