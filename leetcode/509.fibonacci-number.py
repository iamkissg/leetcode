from functools import lru_cache

class Solution:
    
    @lru_cache(maxsize=None)
    def fib(self, N: int) -> int:
        '''
        20190930
        第一次尝试使用 lru_cache, 快得飞起

        with lru_cache
        执行用时 :40 ms, 在所有 Python3 提交中击败了94.85% 的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.54%的用户

        without lru_cache
        执行用时 :940 ms, 在所有 Python3 提交中击败了25.81% 的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.54%的用户
        '''
        if N <= 1:
            return N
        return self.fib(N-1) + self.fib(N-2)

    def fib_dp(self, N: int) -> int:
        '''
        20190930
        执行用时 :40 ms, 在所有 Python3 提交中击败了94.85% 的用户
        内存消耗 :14 MB, 在所有 Python3 提交中击败了5.54%的用户

        诚不我欺, 递归+备忘录时间效率上匹配递推
        '''
        if N <= 1:
            return N
        a, b, = 0, 1
        for i in range(1, N):
            a, b = b, a+b
        return b
    


if __name__ == "__main__":
    sol = Solution()
    print(sol.fib(2))
    print(sol.fib(3))
    print(sol.fib(4))
    print(sol.fib(30))

    print(sol.fib_dp(2))
    print(sol.fib_dp(3))
    print(sol.fib_dp(4))
    print(sol.fib_dp(30))