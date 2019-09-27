class Solution:
    def numWays(self, n: int, k: int) -> int:
        '''
        20190924, 44 ms	13.9 MB	Python3
        我大概是个动态规划白痴, 整理了半天头绪, 毫无头绪
        此解法参考网友的说法:

        从第三根栅栏开始, 前两根颜色相同的情况是 k, 此时只能选不同的颜色, 有 k*(k-1) 种选择
        前两根颜色不同的情况有 k*k-k 种, 此时可以尽情地选择, 于是有 (k*k-k)*k 种选择
        两个合起来, 有 (k-1)(k*k+k), 这个式子的右边看起来很熟悉, 就是 f(n-1)+f(n-2), 不过这里缺少证据是否如此递推就行了
        '''
        if n == 0:
            return 0
        elif n == 1:
            return k
        elif n == 2:
            return k * k
        elif n > 2 and k == 1:
            return 0

        a, b = k, k*k
        for i in range(n-2):
            a, b = b, (a+b)*(k-1)

        return b


    def numWays2(self, n: int, k: int) -> int:
        '''
        再回过头来看, 前两根颜色相同, 这时候只能选不同的颜色, 那么 k*(k-1) 得到的就是新的一根栅栏和前一根不同
        前两根颜色不同的情况, 这时候, 只要选和前一根颜色相同即可, 即 k*k-k 种情况, 剩下的即是两根栅栏颜色不同的情况, (k*k-k)*(k-1)
        所以, 此番过后, 颜色相同的情况是, k*k-k (即 diff(i-1)), 颜色不同的情况, (same(i-1)+diff(i-1))*(k-1)
        60 ms	13.5 MB	Python3
        '''
        if n == 0:
            return 0
        elif n == 1:
            return k
        elif n == 2:
            return k * k
        elif n > 2 and k == 1:
            return 0

        same, diff = k, k*k-k
        for i in range(2, n):
            same, diff = diff, (same+diff)*(k-1)
        return same+diff



if __name__ == "__main__":
    sol = Solution()
    print(sol.numWays(4, 3))
    print(sol.numWays2(4, 3))
    print(sol.numWays(4, 2))
    print(sol.numWays2(4, 2))