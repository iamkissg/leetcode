from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        '''
        20191025
        48 ms	13.7 MB	Python3

        其实没啥好说的, 保持进位吧
        '''
        carry = 1
        res = []
        for a in digits[::-1]:
            carry, val = divmod(a+carry, 10)
            res.append(val)
        return res[::-1] if not carry else [carry] + res[::-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([0]))
    print(sol.plusOne([9]))
    print(sol.plusOne([1, 2]))
    print(sol.plusOne([9, 9]))
    print(sol.plusOne([]))
