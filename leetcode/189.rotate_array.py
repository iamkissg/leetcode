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

        # k 可能大于数组的长度
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]

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