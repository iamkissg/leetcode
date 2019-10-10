from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        min_len = min([len(s) for s in strs])
        if min_len == 0:
            return ""

        common_prefix = ""
        for i in range(min_len):
            # 我居然看不懂自己半年前在写什么...
            # 我这个方法真实太牛逼了, 有点反向思维的意思, 取所有字符串的第 i 位, 构成一个集合, 如何集合的大小为 1, 说明这一位是统一的, 可以加入到公共前缀中.
            if len({s[i] for s in strs}) == 1:
                common_prefix += strs[0][i]
            else:
                break

        return common_prefix

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))
    print(sol.longestCommonPrefix(["dog","racecar","car"]))