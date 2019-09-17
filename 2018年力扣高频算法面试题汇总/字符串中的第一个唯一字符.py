from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        执行用时：84 ms
        '''
        if not s:
            return -1
        
        chars = list(filter(lambda x: x[1]==1, Counter(s).items()))
        if not len(chars):
            return -1
        return min([s.index(c[0]) for c in chars])


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar('leetcode'))
    print(sol.firstUniqChar('loveleetcode'))