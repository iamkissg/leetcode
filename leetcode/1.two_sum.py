from typing import List


class Solution(object):
    def twoSum3(self, nums, target):
        """
        执行用时 :2272 ms, 在所有 Python3 提交中击败了18.15% 的用户
        内存消耗 :14.6 MB, 在所有 Python3 提交中击败了7.81%的用户
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if target-nums[i] in nums:
                if i == nums.index(target-nums[i]):
                    continue
                return [i, nums.index(target-nums[i])] if nums.index(target-nums[i]) > i else [nums.index(target-nums[i]), i]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        '''
        20190918
        执行用时 :1892 ms, 在所有 Python3 提交中击败了20.85% 的用户
        内存消耗 :14.8 MB, 在所有 Python3 提交中击败了6.08%的用户
        '''
        for i, n in enumerate(nums):
            if target - n in set(nums[:i]+nums[i+1:]):
                target_index = (nums[:i]+nums[i+1:]).index(target-n)
                return (i, target_index) if target_index<i else (i, target_index+1)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        终于悟了的解法, 配对问题
        遍历的时候, 假设我自己是 target-n, 我要找 n
        找到了就返回我的 id 和她预留的 id
        没找到就留下我的 id, 让别人来找我

        
        执行用时 :92 ms, 在所有 Python3 提交中击败了52.86% 的用户
        内存消耗 :15.3 MB, 在所有 Python3 提交中击败了5.05%的用户
        '''
        couple = {}
        for i, n in enumerate(nums):
            if n in couple:
                return i, couple[n]
            else:
                couple[target-n] = i


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
    # print(sol.twoSum2([2, 7, 11, 15], 9))
    print(sol.twoSum([3, 2, 4], 6))
    # print(sol.twoSum2([3, 2, 4], 6))
    print(sol.twoSum([3, 3], 6))
    # print(sol.twoSum2([3, 3], 6))