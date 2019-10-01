from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        20190929
        执行用时 :172 ms, 在所有 Python3 提交中击败了52.01% 的用户
        内存消耗 :14.7 MB, 在所有 Python3 提交中击败了5.50%的用户
        '''

        result = []

        len_s = len(s)
        len_p = len(p)
        left, right = 0, len_p-1
        counter_p = Counter(p)
        tmp = Counter(s[left: right])
        need = {k: counter_p[k]-tmp.get(k, 0) for k in counter_p.keys()}

        while right < len_s:
            if s[right] in need:
                need[s[right]] -= 1
            if max(need.values()) <= 0:
                result.append(left)

            if s[left] in need:
                need[s[left]] += 1

            right += 1
            left += 1

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.findAnagrams(s="cbaebabacd", p="abc"))
    print(sol.findAnagrams(s="abab", p="ab"))
            