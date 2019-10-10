from typing import List
from sys import maxsize


INT_MAX = maxsize

class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        if not bulbs or len(bulbs) < 2:
            return -1

        n = len(bulbs)
        ans = INT_MAX
        flowers = [i for i, f in sorted(enumerate(bulbs, start=1), key=lambda t: t[1])]

        l, r = 0, K+1
        while l < n-1-K:
            date = max(flowers[l], flowers[r])

            # 用 all 来判断不如 for-loop 好, for-loop 能及时停止
            # if all(f > date for f in flowers[l+1: r]):
            #     ans = min(ans, date)
            for d in range(l+1, r):
                if flowers[d] < date:
                    # 依然是根据区间不重叠原理, 如果发现一个更小的区间, 直接跳到该位置
                    l, r = d, d+K+1
                    break
            else:
                ans = min(ans, date)
                # 按照 leetcode 题解的说法, 两个可能的候选项, 不能重叠
                # 若 [l1, r1], [l2, r2] 都是候选项, 且 l1<l2<r1<r2
                # 则 flowers[l2] > flowers[r1] 和 flowers[r1] > flowers[l2] 产生矛盾 (在两个区间里, 边界都是最小的)
                l, r = r, r+K+1

        return -1 if ans == INT_MAX else ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.kEmptySlots([3,9,2,8,1,6,10,5,4,7], 1))
    print(sol.kEmptySlots([1, 3, 2], 1))
    print(sol.kEmptySlots([2], 1))
    print(sol.kEmptySlots([], 1))