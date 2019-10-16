class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        n = len(s)
        max_len = 0
        res = ''
        for i, c in enumerate(s):
            left, l_len = self.expand(s, i, i, n)
            right, r_len = self.expand(s, i, i+1, n)
            if max(l_len, r_len) > max_len:
                if l_len > r_len:
                    max_len = l_len
                    res = left
                else:
                    max_len = r_len
                    res = right

        return res

    def expand(self, s, l, r, n):
        while 0<=l and r<n and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r], r-l-1

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome('babad'))
    print(sol.longestPalindrome('cbbd'))