import sys


class Solution:
    def square(self, n: int) -> str:
        if n == 1:
            return '1'
        if n == 2:
            return '121'

        result = ['' for _ in range(2*n-1)]
        m = 2*n-1

        carry = 0
        for val, i in enumerate(range(m-1, n-2, -1), start=1):
            carry, val = divmod(val+carry, 10)
            result[i] = str(val)
        for val in range(n-2, -1, -1):
            i = val
            carry, val = divmod(1+val+carry, 10)
            result[i] = str(val)

        return ''.join(result)
            

if __name__ == "__main__":
    sol = Solution()
    N = int(input())
    print(sol.square(N))