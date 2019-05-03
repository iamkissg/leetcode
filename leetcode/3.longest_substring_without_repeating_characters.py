class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = []
        max_len = 0
        lens = len(s)
        for i, c in enumerate(s):
            if c not in ss:
                ss.append(c)
            else:
                if len(ss) > max_len:
                    max_len = len(ss)
                ss = ss[ss.index(c)+1:]
                ss.append(c)
        else:
            if len(ss) > max_len:
                max_len = len(ss)
        return max_len

if __name__ == "__main__":
    sol = Solution()
    # print(sol.lengthOfLongestSubstring('abcabcbb'))
    # print(sol.lengthOfLongestSubstring('bbbbb'))
    # print(sol.lengthOfLongestSubstring('pwwkew'))
    # print(sol.lengthOfLongestSubstring(" "))
    print(sol.lengthOfLongestSubstring("dvdf"))
    
