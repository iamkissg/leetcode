from typing import List


class Solution:
    '''
    20190930
    执行用时 :104 ms, 在所有 Python3 提交中击败了77.69% 的用户
    内存消耗 :15 MB, 在所有 Python3 提交中击败了5.30%的用户

    好好看了 https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-suan-fa-xi-jie-xiang-jie-by-labula/
    这哥写得太鞭辟入里了!
    我明白了 rihgt 选取决定了搜索区间是左闭右开还是闭区间, 而这又决定了循环终止条件是 left<=right(闭区间), 还是 left<right(左闭右开)
    搜索一个数时, 找到 target 即刻返回; 寻找边界时, 找到 target 并不立即返回, 而是要不断缩小边界, 让循环自然退出
    '''
    def searchLeft(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = (l+r) // 2
            if nums[mid] == target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
        return l

    def searchRight(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = (l+r) // 2
            if nums[mid] == target:
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
        return r-1


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target not in set(nums):
            return (-1, -1)

        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)
        return left, right


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange(nums=[5,7,7,7,8,8,8,8,8,10], target=8))
    print(sol.searchRange(nums=[1,2,3,4,5,6,7,8,8,8,8,9,10], target=8))
    print(sol.searchRange(nums=[5,7,7,8,8,10], target=8))
    print(sol.searchRange(nums=[5,7,7,8,8,10], target=6))
    print(sol.searchRange(nums=[8,8], target=8))
    print(sol.searchRange(nums=[1,4], target=4))
    print(sol.searchRange([1,2,3,3,3,3,4,5,9], 3))

