from functools import reduce
from collections import deque
from math import gcd


class Solution:
    def find_gcd(self, x, y):
        while x%y != 0:
            x, y = y, x%y
        return y
    
    def find_lcm(self, x, y):
        return x*y//self.find_gcd(x, y)


    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        '''
        20190922
        题解来自排行榜的前排, 我的理解是, 用公倍数来去重, 然后用一个很神奇的式子, 计算数在丑数数组中的下标
        1. num//(a|b|c), 意味着 num 分别在 a, b, c 的整数倍数字中的下标,
            1.1. 这部分相加, 计算了不重叠情况下 num 的下标, 可以重叠的数字看作两个数字, 这里如果 num 也被 abc 中多个覆盖, 是重叠数字的第一个下标
        2. 减去 num 在两两最小公倍数的整数倍数字中的下标
            2.1 但是可能会减多了, 比如 12 被 2, 3, 4 整除, 但是会在 23 和 34 和 24 中被减 3 次, 相当于全部剪掉了, 要加回来, 所以有了 +234
        3. 然后用二分查找, 起飞

        *****重要的事情说3遍: 有序数组, 查找, 勿忘二分查找*****
        *****重要的事情说3遍: 有序数组, 查找, 勿忘二分查找*****
        *****重要的事情说3遍: 有序数组, 查找, 勿忘二分查找*****

        我意识到了最小公倍数, 也意识到了重叠的问题, 但是止不于此了.
        '''
        # a, b, c = sorted([a, b, c])
        # lcm_ba = self.find_lcm(a, b)
        # lcm_bc = self.find_lcm(c, b)
        # lcm_ac = self.find_lcm(c, a)
        lcm_ab = a*b//gcd(a, b)
        lcm_bc = b*c//gcd(b, c)
        lcm_ac = a*c//gcd(a, c)
        lcm_abc = lcm_ab*lcm_bc//gcd(lcm_ab, lcm_bc)

        ans = 0
        start, end = 1, 2*10**9
        while start <= end:
            mid = (start+end)//2
            # 这个东西充当了下标
            cnt = mid//a+mid//b+mid//c -(mid//lcm_ab+mid//lcm_ac+mid//lcm_bc) +mid//lcm_abc
            if cnt >= n:
                end = mid-1
                if cnt == n:
                    ans = mid
            else:
                start = mid+1
        return ans

            
    def nthUglyNumber2(self, n: int, a: int, b: int, c: int) -> int:
        '''
        20190922
        尝试沿用丑数2的思路, 但是时间效率上存在严重缺陷, 丑数2规定了 n<=1600+, 但是本题的 n<10^9
        '''
        queues = {i: deque([i]) for i in [a, b, c]}

        for _ in range(n):
            result = min([q[0] for q in queues.values()])
            for i, q in queues.items():
                if result == q[0]:
                    q.popleft()
                    q.append(result + i)
        return result


if __name__ == "__main__":
    sol = Solution()
    # print(sol.find_lcm(2, 3))
    # print(sol.find_lcm(4, 3))
    # print(sol.find_lcm(5, 3))
    # print(sol.find_lcm(15, 25))

    print(sol.nthUglyNumber(n = 3, a = 2, b = 3, c = 5))
    print(sol.nthUglyNumber(n = 4, a = 2, b = 3, c = 4))
    print(sol.nthUglyNumber(n = 5, a = 2, b = 11, c = 13))
    print(sol.nthUglyNumber(n = 1000000000, a = 2, b = 217983653, c = 336916467))

    # print(sol.nthUglyNumber2(n = 3, a = 2, b = 3, c = 5))
    # print(sol.nthUglyNumber2(n = 4, a = 2, b = 3, c = 4))
    # print(sol.nthUglyNumber2(n = 5, a = 2, b = 11, c = 13))
    # print(sol.nthUglyNumber2(n = 1000000000, a = 2, b = 217983653, c = 336916467))