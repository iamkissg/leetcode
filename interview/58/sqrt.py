class Solution:
    def isclose(self, a, b, eps=1e-2):
        return abs(a-b) < eps

    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        l, r = 0, x
        mid = (l+r)/2
        square = mid * mid
        while True:
            mid = (l+r)/2
            square = mid * mid
            if self.isclose(square, x):
                return int(mid)
            if square < x:
                l = mid
            elif square > x:
                r = mid
            
if __name__ == "__main__":
    sol = Solution()
    print(1, sol.mySqrt(1))
    print(2, sol.mySqrt(2))
    print(3, sol.mySqrt(3))
    print(4, sol.mySqrt(4))
    print(8, sol.mySqrt(8))
    print(9, sol.mySqrt(9))
    print(15, sol.mySqrt(15))
    print(16, sol.mySqrt(16))