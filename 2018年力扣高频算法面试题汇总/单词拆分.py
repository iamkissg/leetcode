from typing import List
from functools import reduce


# 暴力解法不可行
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         if s in wordDict:
#             return True
#         positions = []
#         for i in range(1, len(s)):
#             if s[:i] in wordDict:
#                 positions.append(i)
#         if not positions:
#             return False
#         else:
#             positions = reversed(positions)
#             for p in positions:
#                 if self.wordBreak(s[p:], wordDict):
#                     return True
#             else:
#                 return False


# from https://blog.csdn.net/qq_17550379/article/details/82933187
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        len_s = len(s)
        memo = [False] * (len_s+1)  # 多一个表示没有找到单词的情况, 对应最后一个位置
        memo[0] = True
        for i in range(1, len_s+1):
            for w in wordDict:
                # 后两个条件算是相辅相成的
                # memo 表示 s[0:i-len(w)] 没问题, 可以表示成字典中单词的某种组合
                # 然后 w==s[i-len(w):i], 将边界进一步推进到 s[0:i]
                if i >= len(w) and memo[i-len(w)] and w == s[i-len(w):i]:
                    memo[i] = True
        return memo[-1]


if __name__ == "__main__":
    sol = Solution()

    print(sol.wordBreak('leetcode', ['leet', 'code']))
    print(sol.wordBreak('applepenapple', ['apple', 'pen']))
    print(sol.wordBreak('catsandog', ['cat', 'dog', 'cats', 'sand', 'and']))
    print(sol.wordBreak('goalspecial', ["go","goal","goals","special"]))
    print(sol.wordBreak('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab',
                        ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
