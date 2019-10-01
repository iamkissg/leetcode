import re


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        char_vocab = set(s)
        while True:
            lens = len(s)
            i = 0
            while i < len(s):
                if s[i: i+k] == s[i]*k:
                    s = s[:i] + s[i+k:]
                i += 1
            if len(s) == lens:
                break
        return s


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates('deeedbbcccbdaa'*1000, 3))
    print(sol.removeDuplicates('abcd'*100, 2))
    print(sol.removeDuplicates('pbbcggttciiippooaais'*10, 2))
