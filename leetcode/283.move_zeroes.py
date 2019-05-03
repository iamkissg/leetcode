from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            raise ValueError

        move_pointer = len(nums) - 1
        counter = 0
        for item in nums[::-1]:
            if item == 0:
                swap_pointer = move_pointer
                while swap_pointer != len(nums) - 1:
                    nums[swap_pointer], nums[swap_pointer+1] = \
                        nums[swap_pointer+1], nums[swap_pointer]
                    swap_pointer += 1
            move_pointer -= 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.moveZeroes([0, 1, 0, 3, 12]))
    # print(sol.moveZeroes([0]))
    # print(sol.moveZeroes([1, 0]))
    # print(sol.moveZeroes([0, 1]))