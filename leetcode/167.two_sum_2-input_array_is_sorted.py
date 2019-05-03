from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            if target - numbers[i] in numbers[i+1:]:
                if numbers[i] * 2 == target:
                    return i+1, i+2
                else:
                    return i+1, numbers.index(target-numbers[i]) + 1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return i+1, j+1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return []



if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
    print(sol.twoSum([0, 0, 11, 15], 0))
    print(sol.twoSum([5, 25, 75], 100))