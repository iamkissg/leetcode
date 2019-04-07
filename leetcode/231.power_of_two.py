class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return not n & (n-1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfTwo(0))
    print(sol.isPowerOfTwo(1))
    print(sol.isPowerOfTwo(2))
    print(sol.isPowerOfTwo(3))