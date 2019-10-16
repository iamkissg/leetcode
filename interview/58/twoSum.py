from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, a in enumerate(nums):
            if a in d:
                return [d[a], i]
            else:
                d[target-a] = i

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum(nums = [2, 7, 11, 15], target = 9))
    print(sol.twoSum(nums = [2, 2, 11, 3], target = 4))