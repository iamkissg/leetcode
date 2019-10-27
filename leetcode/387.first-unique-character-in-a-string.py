from collections import OrderedDict
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        20191026
        1. 非计数法
        104 ms	13.7 MB	Python3
        '''
        # if not s:
        #     return -1

        # d = OrderedDict()
        # for i, c in enumerate(s):
        #     if c not in d:
        #         d[c] = i
        #     else:
        #         d[c] = -1
        
        # for k, v in d.items():
        #     if v != -1:
        #         return v
        # else:
        #     return -1

        '''
        20191026

        计数法
        76 ms	13.9 MB	Python3
        '''
        valid_keys = list(filter(lambda t: t[1] == 1, Counter(s).items()))
        return -1 if not valid_keys else min([s.index(k[0]) for k in valid_keys])
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar(""))
    print(sol.firstUniqChar("leetcode"))
    print(sol.firstUniqChar("dddccdbba"))