from typing import List


class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     '''
    #     20191005
    #     72 / 75 个通过测试用例
    #     超时
    #     '''
    #     if not nums or len(nums) == 1:
    #         return True

    #     n = len(nums)
    #     for i in range(nums[0], 0, -1):
    #         if i > n:
    #             return True
    #         if self.canJump(nums[i:]):
    #             return True
    #     return False

    def canJump(self, nums: List[int]) -> bool:
        '''
        20191005
        116 ms	15.9 MB	Python3

        网友的解法, 处于懵b状态, 这什么神仙代码?
        解释也看不懂啊:
            如果某一个作为起跳点的格子可以跳跃的距离是3，那么表示后面3个格子都可以作为起跳点。(i+nums[i], 就表示从当前位置起跳的最远位置)
            可以对每一个能作为起跳点的格子都尝试跳一次，把能跳到最远的距离不断更新。(k是当前最远坐标)
            如果可以一直跳到最后，就成功了。
        '''
        k = 0
        n = len(nums)
        for i in range(n):
            if i > k: return False
            k = max(k, i+nums[i])
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([3,0,8,2,0,0,1]))
    print(sol.canJump([2,3,1,1,4]))
    print(sol.canJump([3,2,1,0,4]))
    print(sol.canJump([0,2,3]))
    print(sol.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))