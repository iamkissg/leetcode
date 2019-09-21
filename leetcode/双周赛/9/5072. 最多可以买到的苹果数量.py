from typing import List
from functools import reduce


class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:

        arr.sort()
        if arr[0] > 5000:
            return 0
        elif sum(arr) <= 5000:
            return len(arr)
        accumulated = 0
        ra = []
        for w in arr:
            accumulated += w
            ra.append(accumulated)
        
        start, end = 0, len(arr)
        while start != end-1:
            mid = (start+end) // 2
            if ra[mid] <= 5000:
                start = mid
            else:
                end = mid
        return end

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxNumberOfApples([100,200,150,1000]))
    print(sol.maxNumberOfApples([900,950,800,1000,700,650]))
