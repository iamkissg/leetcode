class Solution:
    def reverse2(self, x: int) -> int:
        '''
        40 ms	13.7 MB	Python3
        '''
        if x == 0:
            return 0
        # if x > 2**31-1 or x < -2**31:
        #     return 0
        
        reversed = int(str(x)[::-1]) if x > 0 else -int(str(x)[1:][::-1])
        return reversed if -2**31 <= reversed <= 2**31-1 else 0

    def reverse(self, x: int) -> int:
        '''
        20190928
        48 ms	13.8 MB	Python3
        '''
        is_negative = bool(x & (1<<31))
        x = abs(x)
        result = 0
        while x:
            x, rest = divmod(x, 10)
            result = result * 10 + rest

        if is_negative:
            result = -result
        return result if -2**31 <= result <= 2**31-1 else 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))
    print(sol.reverse(-123))
    print(sol.reverse(120))
    print(sol.reverse(0))
    print(sol.reverse(1534236469))