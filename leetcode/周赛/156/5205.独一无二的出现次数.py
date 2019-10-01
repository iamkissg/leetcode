from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(counter.values()) == len(set(counter.values()))


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniqueOccurrences([1,2,2,1,1,3]))
    print(sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
    print(sol.uniqueOccurrences([1,2]))