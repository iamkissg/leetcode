from typing import List
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        for i in mat[0][:]:
            for row in mat[1:]:
                if i in row:
                    continue
                else:
                    break
            else:
                return i
        else:
            return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestCommonElement([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]))