class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        res = set()
        n = len(s)
        for i, c in enumerate(s):
            res_left = self.expand(s, i, i, n)
            res_right = self.expand(s, i, i+1, n)
            res.update(res_left)
            res.update(res_right)
        return len(res)
    
    def expand(self, s, l, r, n):
        res = set() if l != r else {(l, r)}
        while 0 <= l and r < n and s[l] == s[r]:
            res.add((l, r))
            l -= 1
            r += 1
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubstrings('abc'))
    print(sol.countSubstrings('a'))
    print(sol.countSubstrings('aa'))