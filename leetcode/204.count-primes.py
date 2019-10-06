class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        20191005
        count: 1228 ms	33.7 MB	Python3
        sum: 828 ms	33.9 MB	Python3

        由于 n 的范围未知, 不方便事先生成素数列表
        '''
        if n < 3:
            return 0

        is_prime = [True for i in range(n)]
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, n):
            if is_prime[i]:
                for j in range(i+i, n, i):
                    is_prime[j] = False

        return is_prime.count(True)

if __name__ == "__main__":
    sol = Solution()
    print(sol.countPrimes(10))
    print(sol.countPrimes(3))
    print(sol.countPrimes(2))