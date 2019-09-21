class Solution:
    def __init__(self):
        self.memo = {}

    def helper(self, x: float, n: int) -> float:
        # n 的取值可以很大, 这样累乘的效率很低, 可以对半乘 
        # n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
        # result = 1.0
        # for _ in range(n):
        #     result *= x
        # return result

        # 执行用时 :40 ms, 在所有 Python3 提交中击败了96.53% 的用户
        if (x, n) in self.memo:
            return self.memo[(x, n)]

        if n == 1:
            return x
        elif n == 2:
            return x*x

        self.memo[(x, n//2)] = self.helper(x, n//2)
        result = self.memo[(x, n//2)] * self.memo[(x, n//2)]
        result *= x if n & 1 else 1
        return result

    def iterative_helper(self, x: float, n: int) -> float:
        result = 1.0
        while n:
            # 这个式子太神奇了
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result




    def myPow(self, x: float, n: int) -> float:
        # 特例不能忘
        if x == 0:
            if n < 0:
                raise ZeroDivisionError()
            elif n == 0:
                return 1.0
            else:
                return 0.0
        if n == 0:
            return 1.0

        if n < 0:
            result = 1/self.helper(x, -n)
        else:
            result = self.iterative_helper(x, n)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2, 5))
    print(pow(2, 3))