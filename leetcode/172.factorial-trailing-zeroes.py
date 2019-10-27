class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        20191022
        44 ms	13.9 MB	Python3

        基本思想是: 只有 2*5 能得到 0, 所以求阶乘中 0 的个数, 相当于求阶乘的因式分解中 2 和 5 的个数
        而 5 的个数会比 2 少, 所以问题最终转化为求 5 的个数
        解法 2 还是相对很奇葩的
        '''
        res = 0

        # 解法一, 会超时
        # for i in range(5, n+1, 5):
        #     j = i
        #     while not j%5:
        #         j //= 5
        #         res += 1

        # 编程之美的解法2: 统计 [N//5]+[N//25]+[N//125]+...
        # [N//5] 表示 5 的倍数贡献一个 5, 合起来总共贡献了 N//5 个 5;
        # [N//25] 表示 25 的倍数再贡献一个 5, 合起来又贡献了 N//25 个 5; 
        # 依次类推
        while n:
            res += n // 5
            n //= 5

        return res