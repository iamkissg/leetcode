from math import sqrt, floor


class Solution:

    # 递归不可行, 因为包含一个 1, 在事先不知道四平方数定理的情况下, 最常的路径会导致栈被撑爆.
    # def numSquares(self, n: int) -> int:
    #     if n in self.memo:
    #         return self.memo[n]
    #     result = min([self.numSquares(n-i**2) for i in range(1, floor(sqrt(n))+1)])+1
    #     self.memo[n] = result
    #     return result


    # 将 memo 从 `def __init__(self)` 中取出来是关键, 从实例变量变成了类变量, 作弊啊
    # 176 ms
    memo = {0: 0, 1: 1}
    def numSquares(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        i = 1
        while n not in self.memo:
            i += 1
            if i in self.memo:
                continue
            self.memo[i] = min((self.memo[i-j*j] for j in range(1, floor(sqrt(i))+1))) + 1
        return self.memo[n]
        



if __name__ == "__main__":
    sol = Solution()
    print(sol.memo)
    for i in [12,2,3,4,5,6,7,8,9,10,5373,5374]:
        print(sol.numSquares(i))

    print('='*80)
    print(sol.numSquares(2))
    print(sol.numSquares(8))
    print(sol.numSquares(10))
    print(sol.numSquares(11))
    print(sol.numSquares(12))
    print(sol.numSquares(13))
    print(sol.numSquares(5673))
    print(sol.numSquares(5674))
    