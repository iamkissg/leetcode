from typing import List

# __author__ = 'iamkissg'
# __date__ = '20190921'


class Solution:

    def countBit(self, n: int) -> int:
        '''
        一个数与上比它小一的数, 会把它最后一位的 1 打掉
        '''
        if n < 0:
            raise Exception('')
        
        res = 0
        while n:
            n &= n-1
            res += 1
        return res

    def countBits(self, num: int) -> List[int]:
        # 152 ms	19.9 MB
        # 对每个数字都求它的 1 的位数
        result = [self.countBit(i) for i in range(num+1)]
        return result


    def countBits2(self, num: int) -> List[int]:
        # 92 ms	20.1 MB
        counter = [0] * (num+1)
        for i in range(1, num+1):
            counter[i] = counter[i&(i-1)] + 1
        return counter


if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits2(5))
    print(sol.countBits2(0))
    print(sol.countBits2(1))
    print(sol.countBits2(11))
