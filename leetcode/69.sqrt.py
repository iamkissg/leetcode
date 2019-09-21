from math import ceil, isclose

class Solution:
    def mySqrt(self, x: int) -> int:
        '''20190921'''
        # 56 ms	13.9 MB	Python3
        if x <= 1:
            return x

        start = 0
        end = x
        while start != end-1:
            mid = (start + end) // 2
            # 这一条件能保证了 end 大于根号 x, 于是等到循环结束的时候, start 正是要找的
            if mid ** 2 <=x:
                start = mid
            else:
                end = mid
        return start

    def mySqrt(self, x: int) -> int:
        '''20190921'''
        if x <= 1:
            return x

        cur = 1
        while True:
            cur, pre = (cur+x/cur)/2, cur

            # 运行速度取决于精度
            # 48 ms	13.8 MB	Python3, default, rel_tol=1e-9, 相对误差
            # 68 ms	13.9 MB	Python3, default, rel_tol=1e-9, 相对误差
            if isclose(cur, pre):
                return int(cur)



if __name__ == "__main__":
    sol = Solution()
    # print(sol.mySqrt(0))
    # print(sol.mySqrt(1))
    print(sol.mySqrt(2))
    print(sol.mySqrt(3))
    print(sol.mySqrt(8))
    print(sol.mySqrt(9))
    print(sol.mySqrt(15))