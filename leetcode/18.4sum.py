
class Solution:

    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        20190918
        来自覃超的另一种解法
        遍历一遍, 然后从剩余的数字中凑
        
        执行用时 :988 ms, 在所有 Python3 提交中击败了85.78% 的用户
        内存消耗 :16.7 MB, 在所有 Python3 提交中击败了79.82%的用户
        '''
        if len(nums) < 3:
            return []

        result = set()
        for i, a in enumerate(nums[:-2]):
            # 因为已经排序过了, a==nums[i-1], 意味着重复数字
            if i >= 1 and a == nums[i-1]:
                continue
            # d 的做法和 2sum 的解法思路一致, 如果没有找到想要的 (b), 那我先把我自己的信息留下 (-a-b)
            d = {}
            for j, b in enumerate(nums[i+1:]):
                if b not in d:
                    d[target-a-b] = 1
                else:
                    result.add((a, target-a-b, b))
        return list(result)

    def fourSum(self, nums, target):
        len_nums = len(nums)
        if len_nums < 4:
            return []
        
        nums.sort()
        result = set()
        for i, a in enumerate(nums[:-3]):
            if i >= 1 and a == nums[i-1]:
                continue
            three_sum = self.threeSum(nums[i+1:], target-a)
            result.update((a)+item for item in three_sum)

        return result

        

