from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            raise ValueError('Empty list')

        jinwei = 1
        lend = len(digits)
        for i in range(len(digits)):
            jinwei, digits[lend-i-1] = divmod(digits[lend-i-1]+jinwei, 10)
        return [jinwei] + digits if jinwei else digits


if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([0]))
    print(sol.plusOne([9]))
    print(sol.plusOne([1, 2]))
    print(sol.plusOne([9, 9]))
    print(sol.plusOne([]))
