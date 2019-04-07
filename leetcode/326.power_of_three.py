class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        elif n % 3:
            return False
        else:
            while n:
                n /= 3
                if n == 1:
                    return True
                if n % 3:
                    return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfThree(-1))
    print(sol.isPowerOfThree(0))
    print(sol.isPowerOfThree(1))
    print(sol.isPowerOfThree(2))
    print(sol.isPowerOfThree(3))
    print(sol.isPowerOfThree(6))
    print(sol.isPowerOfThree(9))