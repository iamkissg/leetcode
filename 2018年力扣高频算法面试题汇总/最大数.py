from typing import List


from functools import cmp_to_key


class Solution:
    # https://shenjie1993.gitbooks.io/leetcode-python/179%20Largest%20Number.html
    def largestNumber(self, nums: List[int]) -> str:
        str_num =  ''.join(sorted(map(str, nums),
                                  key=cmp_to_key(lambda x, y: int(y+x)-int(x+y)),
                                  reverse=False))
        str_num = str_num.lstrip('0')
        return str_num or '0'

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestNumber([3,30,34,5,9]))
    print(sol.largestNumber([10, 2]))