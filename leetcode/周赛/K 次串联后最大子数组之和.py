from typing import List


class Solution:
    MOD = 10^9 + 7

    def maxSum(self, arr: List[int]) -> int:
        for i in range(1, len(arr)):
            if arr[i-1] > 0:
                arr[i] += arr[i-1]
        return max(arr)


    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if all([i >= 0 for i in arr]):
            return sum(arr) * k % self.MOD
        elif all([i <= 0 for i in arr]):
            return 0

        result = 0
        return result