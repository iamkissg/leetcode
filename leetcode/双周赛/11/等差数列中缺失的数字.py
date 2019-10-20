from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        
        n = len(arr)
        diff = (arr[-1]-arr[0]) // n
        if diff == 0:
            return arr[0]

        start = arr[0]
        for i in range(1, n):
            start += diff
            if start not in arr:
                return start

if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber(arr = [5,7,11,13]))
    print(sol.missingNumber(arr = [0, 0, 0, 0]))
    print(sol.missingNumber(arr = [15,13,12]))