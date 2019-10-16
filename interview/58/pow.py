class Solution:
    def __init__(self):
        self.memo = {}

    def myPow(self, x: float, n: int) -> float:
        '''
        20191013
        先按递归的方式写
        '''

        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 1:
            return x

        hash = ':'.join(map(str, [x, n]))
        if hash in self.memo:
            return self.memo[hash]
        
        res = (x if n & 1 else 1) * self.myPow(x, n//2) * self.myPow(x, n//2)
        self.memo[hash] = res
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.0, 10))
    print(sol.myPow(2.1, 3))
    print(sol.myPow(2.0, -2))