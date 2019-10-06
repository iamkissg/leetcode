from typing import List

class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     '''
    #     20191005
    #     执行用时 :56 ms, 在所有 Python3 提交中击败了80.23% 的用户
    #     内存消耗 :14.1 MB, 在所有 Python3 提交中击败了5.73%的用户

    #     假的解法
    #     '''
    #     try:
    #         return nums.index(target)
    #     except ValueError:
    #         return -1

    def search(self, nums: List[int], target: int) -> int:
        min_index = nums.index(min(nums))


if __name__ == "__main__":
    sol = Solution()
    print(sol.search(nums = [4,5,6,7,0,1,2], target = 0))
    print(sol.search(nums = [4,5,6,7,0,1,2], target = 3))