class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        20191002
        116 ms	13.7 MB	Python3
        
        朴素解法, 最少重复 2 次, 一直延长子串到一半的位置
        '''
        if not s:
            return False
        
        n = len(s)
        for i in range(1, n//2+1):
            subs = s[:i]
            quotients, remainder = divmod(n, len(subs))
            if remainder:
                continue
            if subs * quotients == s:
                return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.repeatedSubstringPattern('abab'))
    print(sol.repeatedSubstringPattern('aba'))
    print(sol.repeatedSubstringPattern('a'))
    print(sol.repeatedSubstringPattern(''))
    print(sol.repeatedSubstringPattern('aa'))
    print(sol.repeatedSubstringPattern('abcabcabcabc'))