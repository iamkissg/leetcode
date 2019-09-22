from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if not arr: return [[]]

        arr.sort()

        min_diff = arr[-1]-arr[0]
        result = []
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] < min_diff:
                result = [[arr[i], arr[i+1]]]
                min_diff = arr[i+1]-arr[i]
            elif arr[i+1]-arr[i] == min_diff:
                result.append([arr[i], arr[i+1]])
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumAbsDifference([4,2,1,3]))
    print(sol.minimumAbsDifference([1,3,6,10,15]))
    print(sol.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))