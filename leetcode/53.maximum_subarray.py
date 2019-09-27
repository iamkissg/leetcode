from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if all([n >= 0 for n in nums]):
            return sum(nums)
        if all([n <= 0 for n in nums]):
            return max(nums)
        
        suba = []
        max_val = min(nums)
        max_suba = [max_val]
        for n in nums:
            if not suba and n < 0:
                continue
            if n >= 0:
                suba.append(n)
                if sum(suba) > max_val:
                    max_val = sum(suba)
                    max_suba = suba[:]
            else:
                suba.append(n)
                if sum(suba) < 0:
                    suba = []
        return max_val

    def maxSubArray2(self, nums: List[int]) -> int:
        '''
        执行用时 :88 ms, 在所有 Python3 提交中击败了78.03% 的用户
        内存消耗 :14.7 MB, 在所有 Python3 提交中击败了5.04%的用户
        '''
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1]+nums[i], nums[i])
        print(nums)
        return max(nums)

    def maxSubArray3(self, nums: List[int]) -> int:
        '''
        执行用时 :88 ms, 在所有 Python3 提交中击败了78.03% 的用户
        内存消耗 :14.7 MB, 在所有 Python3 提交中击败了5.04%的用户
        '''
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        print(nums)
        return max(nums)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-6,4]))
    print(sol.maxSubArray2([-2,1,-3,4,-1,2,1,-6,4]))
    print(sol.maxSubArray3([-2,1,-3,4,-1,2,1,-6,4]))
    print(sol.maxSubArray3([1,-2,1]))