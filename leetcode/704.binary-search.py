from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        20190930
        执行用时 :308 ms, 在所有 Python3 提交中击败了76.24% 的用户
        内存消耗 :15.2 MB, 在所有 Python3 提交中击败了5.20%的用户

        在这里, 我让 r 指向待查找区间 [] 的后一位
        '''
        if not nums:
            return -1

        l, r = 0, len(nums)
        while l < r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid
            else:
                return mid
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.search( nums = [], target = 9))
    print(sol.search( nums = [9], target = 9))
    print(sol.search( nums = [1,9], target = 9))
    print(sol.search( nums = [-1,0,3,5,9,12], target = 9))
    print(sol.search( nums = [-1,0,3,5,9,12], target = 2))
            