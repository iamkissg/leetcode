from typing import List


class Solution:
    def is_overlapped(self, a, b):
        return a[1] >= b[0] and a[0] <= b[1]

    def merge_intervals(self, a, b):
        return [min(a[0], b[0]), max(a[1], b[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        20190923
        这个解法有点蠢萌蠢萌的感觉, 啰嗦, 还绕
        128 ms	15.8 MB	Python3
        '''

        intervals = sorted(intervals, key=lambda t: t[1])

        while any([self.is_overlapped(intervals[i], intervals[i+1]) for i in range(len(intervals)-1)]):
            tmp = []
            while len(intervals) > 1:
                a = intervals.pop()
                b = intervals.pop()
                if self.is_overlapped(a, b):
                    merged = self.merge_intervals(a, b)
                    tmp.append(merged)
                else:
                    intervals.append(b)
                    tmp.append(a)

            intervals = sorted(tmp+intervals, key=lambda t: t[1])
            if len(intervals) == 1:
                break

        return intervals

    def merge_by_sorting(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        20190923,
        方法是看了 Leetcode-cn 上的官方题解, 自己写了一遍
        运行效率上居然还不如上面蠢萌蠢萌的方法, 我是有点难以置信的, 因为上面的方法涉及到多次 sort 以及比较区间是否重叠
        176 ms	15.7 MB	Python3
        '''
        intervals = sorted(intervals, key=lambda t: (t[0], t[1]))

        merged = []
        for p in intervals:
            if not merged or merged[-1][1] < p[0]:
                merged.append(p)
            elif p[0] <= merged[-1][1]:
                merged[-1][1] = max(p[1], merged[-1][1])
        return merged


if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(sol.merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))
    print(sol.merge([[1,4],[4,5]]))
    print(sol.merge([[1,4],[0,2],[3,5]]))

    print(sol.merge_by_sorting([[1,3],[2,6],[8,10],[15,18]]))
    print(sol.merge_by_sorting([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))
    print(sol.merge_by_sorting([[1,4],[4,5]]))
    print(sol.merge_by_sorting([[1,4],[0,2],[3,5]]))