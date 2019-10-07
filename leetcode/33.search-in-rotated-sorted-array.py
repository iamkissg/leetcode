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
        '''
        20191007

        64 ms	13.9 MB	Python3
        浏览 Solution 的时候受到网友的点拨: 依然可以使用二分查找, 旋转数组的特点是, 一分为二之后, 一边依然是旋转数组, 另一边是有序数组
        对于有序数组一边, 先用二分查找进行搜索 target, 如果没有找到, 说明 target 可能在另一边, 递归地处理即可

        在下面的实现中, 为了避免"传递子数组, 需要控制下标", 我总是传递整个数组, 并附上了当前的搜索区间边界.
        '''
        if not nums:
            return -1

        l, r = 0, len(nums)-1
        return self.search_spin(nums, target, l, r)

    def search_spin(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left == right:
            return -1 if nums[left] != target else left

        mid = left + (right-left)//2
        if nums[left] < nums[mid]:
            # 左边有序
            find_left = self.binary_search(nums, target, left, mid)
            if find_left != -1:
                return find_left
            return self.search_spin(nums, target, mid+1, right)
        else:
            # 左边无序
            find_right = self.binary_search(nums, target, mid+1, right)
            if find_right != -1:
                return find_right
            return self.search_spin(nums, target, left, mid)



    def binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:
        '''
        include right
        '''

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.search(nums = [4,5,6,7,0,1,2], target = 0))
    print(sol.search(nums = [4,5,6,7,0,1,2], target = 3))