class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        # if x > 2**31-1 or x < -2**31:
        #     return 0
        
        reversed = int(str(x)[::-1]) if x > 0 else -int(str(x)[1:][::-1])
        return reversed if -2**31 <= reversed <= 2**31-1 else 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))
    print(sol.reverse(-123))
    print(sol.reverse(120))
    print(sol.reverse(0))
    print(sol.reverse(1534236469))