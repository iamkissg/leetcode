from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if not arr:
            return 0
        
        n = len(arr)
        dp = [1 for _ in range(n)]
        pos = {arr[0]: 0}
        for i, a in enumerate(arr[1:], start=1):
            pre_pos = pos.get(a-difference, -1)
            if pre_pos != -1:
                dp[i] = dp[pre_pos] + 1
            pos[a] = i
        return max(dp)

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubsequence(arr = [], difference = -2))
    print(sol.longestSubsequence(arr = [2], difference = 1))
    print(sol.longestSubsequence(arr = [1,5,7,8,5,3,4,2,1], difference = -2))
    print(sol.longestSubsequence(arr = [1,2,3,4], difference = 1))
    print(sol.longestSubsequence(arr = [1,2,3,4], difference = 2))
    print(sol.longestSubsequence(arr = [1,3,5,7], difference = 1))