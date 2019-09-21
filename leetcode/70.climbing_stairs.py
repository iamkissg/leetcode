class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            raise ValueError
        if n <= 1:
            return n
        a, b = 1, 2
        for _ in range(2, n):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(1))
    print(sol.climbStairs(2))
    print(sol.climbStairs(3))
    print(sol.climbStairs(0))
    print(sol.climbStairs(-1))