from typing import List


class Solution:

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        '''
        20191002
        888 ms	18.3 MB	Python3  # 使用 nums 作为 hash
        864 ms	18.6 MB	Python3  # 在 canIWin 中定义 memo, 使用 nums 作为 hash
        1024 ms	18.7 MB	Python3  # 修改了 helper 中的 hash
        1020 ms	18.6 MB	Python3  # 修改了 helper 中的 hash, 在 canIWin 中定义 memo

        我感觉我就是个蠢蛋, 执着于寻找速成指南, 但是看到题目脑子一篇空白, 傻了吧唧的
        
        '''

        # 按照网友的说法, 取尽数组也达不到阈值, 游戏无限进行下去, 判 False
        if (1+maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False

        self.memo = {}
        nums = [i for i in range(1, maxChoosableInteger+1)]
        return self.helper(nums, desiredTotal)

    def helper(self, nums: List[int], threshold: int):
        hash = str(nums)
        # hash = str((nums, threshold))
        if hash in self.memo:
            return self.memo[hash]

        if nums[-1] >= threshold:
            return True

        for i, n in enumerate(nums):
            if not self.helper(nums[:i]+nums[i+1:], threshold-n):
                self.memo[hash] = True
                return True
        else:
            self.memo[hash] = False
            return False


if __name__ == "__main__":
    sol = Solution()

    print(sol.canIWin(10, 11))
    print(sol.canIWin(10, 40))