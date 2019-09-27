class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        20190925
        这里的 sub sequence 可以是不连续的, 所以用指针一步步往后移
        '''
        if not s:
            return True
        if not t:
            return False

        ps, pt = 0, 0
        ls, lt = len(s), len(t)
        while ps < ls and pt < lt:
            if s[ps] == t[pt]:
                ps += 1
                pt += 1
            else:
                pt += 1
        if ps == ls:
            return True
        else:
            return False