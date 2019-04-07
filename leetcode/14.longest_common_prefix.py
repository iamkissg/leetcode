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
            if len({s[i] for s in strs}) == 1:
                common_prefix += strs[0][i]
            else:
                break

        return common_prefix

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))
    print(sol.longestCommonPrefix(["dog","racecar","car"]))