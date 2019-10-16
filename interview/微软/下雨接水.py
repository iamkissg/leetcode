from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        20191014
        网友提示的双指针解法: https://leetcode-cn.com/problems/trapping-rain-water/solution/si-zhi-zhen-fa-by-cycoe/
        经网友点拨之后, 一次就通过了

        这类问题之前遇到过的, 具体是干什么的忘记了, 也是求木桩中的水量, 也是双指针法, 也是先移动较短的那一根, 要想起来啊
        '''
        if not height:
            return 0

        n = len(height)
        res = 0
        # l, r = 0, n-1
        for l in range(n):
            if height[l] > 0: break
        for r in range(n-1, -1, -1):
            if height[r] > 0: break
        while l < r:
            if height[l] <= height[r]:
                h = height[l]
                for i in range(l+1, r+1):
                    if height[i] > h: break
                res += sum(h-height[j] for j in range(l, i))
                l = i
            else:
                h = height[r]
                for i in range(r-1, l-1, -1):
                    if height[i] > h: break
                res += sum(h-height[j] for j in range(i+1, r+1))
                r = i
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(sol.trap([2,1,0,2]))
    print(sol.trap([5,2,1,2,1,5]))