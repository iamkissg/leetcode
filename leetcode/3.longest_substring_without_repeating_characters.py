class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        这个解法, 现在看起来有点有点奇怪,
        因为后面用了 ss=ss[ss.index(c)+1:] 这样奇怪的语句, 不过相比滑动窗口, 会更高效一点吧, 直接跳到了重复字符之后
        执行用时 :68 ms, 在所有 Python3 提交中击败了98.22% 的用户
        内存消耗 :14 MB, 在所有 Python3 提交中击败了5.01%的用户
        '''
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


    def lengthOfLongestSubstring_slide_window(self, s: str) -> int:
        '''
        20190922
        通过	92 ms	13.9 MB	Python3
        实践证明, 直接跳到重复字符串之后的效率更高
        '''
        if not s:
            return 0
        p1, p2 = 0, 1
        lens = len(s)

        used_char_set = {s[0]}
        max_len = 1
        while p2 < lens:
            if s[p2] in used_char_set:
                used_char_set.remove(s[p1])
                p1 += 1
            else:
                used_char_set.add(s[p2])
                if len(used_char_set) > max_len:
                    max_len = len(used_char_set)
                p2 += 1
        return max_len


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring('abcabcbb'))
    print(sol.lengthOfLongestSubstring_slide_window('abcabcbb'))
    print(sol.lengthOfLongestSubstring('bbbbb'))
    print(sol.lengthOfLongestSubstring_slide_window('bbbbb'))
    print(sol.lengthOfLongestSubstring('pwwkew'))
    print(sol.lengthOfLongestSubstring_slide_window('pwwkew'))
    print(sol.lengthOfLongestSubstring(" "))
    print(sol.lengthOfLongestSubstring_slide_window(" "))
    print(sol.lengthOfLongestSubstring("dvdf"))
    print(sol.lengthOfLongestSubstring_slide_window("dvdf"))
    
