class Solution:
    def addDigits(self, num: int) -> int:
        # num is a natural number
        if num == 0:
            return 0

        return num % 9 if num % 9 else 9


if __name__ == "__main__":
    sol = Solution()
    print(sol.addDigits(1))
    print(sol.addDigits(10))
    print(sol.addDigits(11))
    print(sol.addDigits(2035))
    print(sol.addDigits(78))