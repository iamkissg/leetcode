from typing import List


from collections import Counter
class Solution:
    def distance(self, a, b):
        return (a[0]-b[0])**2 + (a[1]-b[1])**2

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        '''
        20191020
        1712 ms	30.8 MB	Python3

        本题有一个隐性要求, 构成回旋表的 3 个点, 要交于其中一个点, 即题目中 (i, j, k) 中的 i
        我一开始没有注意这一点, 只是粗暴地统计相同距离的数量, 然后求排列, 这时候对第二个测试用力, 甚至结果数都超过了 A_5_2, 明显不对
        因此, 改成了第二种统计距离的方法, 即针对每个点, 计算与它相距为 n 的点的数量
        '''
        # distances = Counter([self.distance(p, n) for i, p in enumerate(points[:-1]) for n in points[i+1:]])
        distances = {tuple(p): Counter([self.distance(p, n) for j, n in enumerate(points) if j != i]) for i, p in enumerate(points)}
        res = 0
        for p in points:
            tp = tuple(p)
            for k, v in distances[tp].items():
                if v >= 2:
                    res += v*(v-1)
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfBoomerangs([[0,0],[1,0],[2,0]]))
    print(sol.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))