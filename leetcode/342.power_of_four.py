class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        """预构 4 的指数, 空间换时间"""
        if num <= 0:
            return False
        power_of_four_s = {4 << i for i in range(0, 31, 2)}
        power_of_four_s.add(1)
        return num in power_of_four_s

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfFour(0))
    print(sol.isPowerOfFour(1))
    print(sol.isPowerOfFour(2))
    print(sol.isPowerOfFour(4))
    print(sol.isPowerOfFour(8))
    print(sol.isPowerOfFour(16))
