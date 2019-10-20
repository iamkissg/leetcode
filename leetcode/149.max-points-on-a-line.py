from typing import List
import decimal


from math import cos
class Solution:
    def get_w_b(self, p, n):
        if p[1] == n[1]:
            return (0, p[1])
        elif p[0] == n[0]:
            return (float('inf'), p[0])
        else:
            w = decimal.Decimal(n[1]-p[1])/decimal.Decimal(n[0]-p[0])
            b = p[1] - p[0] * w
            return (w, b)

    def maxPoints(self, points: List[List[int]]) -> int:
        '''

        根据测试用例, 点是可以重复的
        '''
        if not points:
            return 0
        if len(points) == 1:
            return 1
        
        points_tuple = list(map(tuple, points))
        d = {}
        for i, p in enumerate(points_tuple):
            for j, n in enumerate(points_tuple):
                if i != j:
                    hash = self.get_w_b(p, n)
                    if hash not in d:
                        d[hash] = {(i, p), (j, n)}
                    else:
                        d[hash].update({(i, p), (j, n)})

        sd = sorted(d.items(), key=lambda t: len(t[1]))
        return len(sd[-1][1])

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPoints([[0,0],[94911151,94911150],[94911152,94911151]]))
    print(sol.maxPoints([[0,0],[0,0]]))
    print(sol.maxPoints([[1,1],[2,2],[3,3]]))
    print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))

