from typing import List


class Solution:

    def is_huiwen(sel, s):
        if not s or len(s) == 1:
            return True

        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]

        result = [[s]] if self.is_huiwen(s) else []
        for i in range(1, len(s)):
            if self.is_huiwen(s[:i]):
                partitioned = self.partition(s[i:])
                # print(s[:i], partitioned)
                for p in partitioned:
                    result.append([s[:i]]+p)
        return result

if __name__ == "__main__":
    sol = Solution()

    print(sol.partition('aab'))
    print(sol.partition('aabb'))
    print(sol.partition('aabaab'))
    print(sol.partition('abbab'))
