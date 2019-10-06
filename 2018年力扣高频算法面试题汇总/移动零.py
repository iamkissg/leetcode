from typing import List


class Solution:
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        20191001
        常规思路 O(n^2), 从后往前找 0, 找到之后移到最后
        """
        len_nums = len(nums)
        for i in range(len_nums-1, -1, -1):
            if nums[i] != 0:
                continue
            for j in range(i, len_nums-1):
                if nums[j] == 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        print(nums)

    def moveZeroes(self, nums: List[int]) -> None:
        '''
        20191002
        执行用时 :60 ms, 在所有 Python3 提交中击败了95.87% 的用户
        内存消耗 :15 MB, 在所有 Python3 提交中击败了6.26%的用户
        双指针法真的厉害了!
        一个指针用于指向 0, 一个则一直向前, 只要一直向前的指针遇到了不为 0 的值, 就交换两个指针的值
        零指针从0位置出发, 遇到非零元素, 零指针和非零指针会一起向前走, 直到遇到零停驻, 然后非零指针继续向前, 遇到非零指针, 两者交换元素
        '''
        zero_pos = 0
        for not_zero_pos in range(len(nums)):
            if nums[not_zero_pos] != 0:
                nums[not_zero_pos], nums[zero_pos] = nums[zero_pos], nums[not_zero_pos]
                zero_pos += 1
        print(nums)

if __name__ == "__main__":
    sol = Solution()
    sol.moveZeroes([1, 2, 3, 0, 0, 1, 2, 3, 4])
    sol.moveZeroes([0,1,0,3,12])
    sol.moveZeroes([1, 0, 3, 0, 2])
    sol.moveZeroes([0, 0, 1])