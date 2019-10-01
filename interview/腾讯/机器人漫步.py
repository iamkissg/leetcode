from itertools import combinations


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n > m:
            return self.uniquePaths(n, m)
        if n == 1 or m == 1:
            return 1
        
        a = n-1
        b = n+m-2
        result = 1
        for i in range(0, a):
            result *= (b-i)
        for i in range(1, a+1):
            result /= i
        return int(result)
        # return max(len(l1ist(combinations(range(n+m-2), n-1))), 0)
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(2, 3))
    print(sol.uniquePaths(7, 3))
    print(sol.uniquePaths(2, 2))
    print(sol.uniquePaths(12, 23))