from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        执行用时：288 ms
        """
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
                 


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseString(list('main')))
