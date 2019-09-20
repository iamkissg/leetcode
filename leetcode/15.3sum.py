from typing import List


class Solution:
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        '''
        20190918
        题解来自覃超的算法课. 代码的写得很简洁很紧凑, 几乎是每一句都缺一不可

        return list(result)
        执行用时 :1636 ms, 在所有 Python3 提交中击败了32.59% 的用户
        内存消耗 :17.3 MB, 在所有 Python3 提交中击败了20.70%的用户

        return map(list, result)
        和前一种返回方法比起来, map 明显比 list 更高效
        执行用时 :1256 ms, 在所有 Python3 提交中击败了55.64% 的用户
        内存消耗 :17.5 MB, 在所有 Python3 提交中击败了14.12%的用户
        '''
        if len(nums) < 3:
            return []

        result = set()
        nums.sort()  # 先 sort 有助于排重, 题设要求不重复
        for i, a in enumerate(nums[:-2]):
            # 因为已经排序过了, a==nums[i-1], 意味着重复数字
            if i >= 1 and a == nums[i-1]:
                continue
            # d 的做法和 2sum 的解法思路一致, 如果没有找到想要的 (b), 那我先把我自己的信息留下 (-a-b)
            d = {}
            for j, b in enumerate(nums[i+1:]):
                if b not in d:
                    d[-a-b] = 1
                else:
                    result.add((a, -a-b, b))
        return list(result)


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        20190918
        来自覃超的另一种解法
        遍历一遍, 然后从剩余的数字中凑
        
        执行用时 :988 ms, 在所有 Python3 提交中击败了85.78% 的用户
        内存消耗 :16.7 MB, 在所有 Python3 提交中击败了79.82%的用户
        '''
        len_nums = len(nums)
        if len_nums < 3:
            return []
        
        result = set()
        nums.sort()
        for i, a in enumerate(nums[:-2]):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len_nums-1
            while l < r:
                s = nums[l] + nums[r] + a
                if s < 0: l += 1
                elif s > 0: r -= 1
                else:
                    result.add((a, nums[l], nums[r]))
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
        return map(list, result)

    
if __name__ == "__main__":
    sol = Solution()
    # print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
    # print(sol.threeSum([0, 0, 0]))
    print(sol.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4]))