from math import ceil

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            raise ValueError('Compute square root on negative integer')
        if x <= 1:
            return x

        start = 1
        end = x//2+1
        mid = (start + end) // 2
        while True:
            if start + 1 == end:
                return start
            if mid ** 2 == x:
                return mid
            if mid ** 2 > x:
                end = mid
                mid = (start + end) // 2
            elif mid ** 2 < x:
                start = mid
                mid = (start + end) // 2



if __name__ == "__main__":
    sol = Solution()
    # print(sol.mySqrt(0))
    # print(sol.mySqrt(1))
    print(sol.mySqrt(2))
    print(sol.mySqrt(3))
    print(sol.mySqrt(8))
    print(sol.mySqrt(9))
    print(sol.mySqrt(15))