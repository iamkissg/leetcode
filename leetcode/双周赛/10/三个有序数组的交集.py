from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(set(arr1).intersection(set(arr2)).intersection(arr3))

if __name__ == "__main__":
    sol = Solution()
    print(sol.arraysIntersection(arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]))