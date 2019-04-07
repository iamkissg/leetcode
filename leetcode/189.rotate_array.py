from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        else:
            len_nums = len(nums)
            k = k % len_nums
            for i in range(k):
                # nums[len_nums-i-1], nums[k-i-1] = nums[k-i-1], nums[len_nums-i-1]
                nums.insert(0, nums.pop())

    def rotate2(self, nums: List[int], k: int) -> None:
        """最快"""
        if not nums or len(nums) == 1:
            return
        else:
            len_nums = len(nums)
            k = k % len_nums
            # 更新了 nums 的引用, 但旧的 nums 的值不变
            # nums = nums[len_nums-k:] + nums[:len_nums-k]
            nums[:] = nums[len_nums-k:] + nums[:len_nums-k]

    def rotate3(self, nums: List[int], k: int) -> None:
        if not nums or len(nums) == 1:
            return
        else:
            from queue import deque

            len_nums = len(nums)
            k = k % len_nums
            que = deque(nums)
            que.rotate(k)
            nums[:] = list(que)


if __name__ == "__main__":
    sol = Solution()

    print(sol.rotate2([1,2,3,4,5,6,7], 3))