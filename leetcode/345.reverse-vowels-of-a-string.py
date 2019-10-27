class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s

        yuanyin = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l, r = 0, len(s)-1
        ls = list(s)
        while l < r:
            if ls[l] not in yuanyin:
                l += 1
                continue
            if ls[r] not in yuanyin:
                r -= 1
                continue
            ls[l], ls[r] = ls[r], ls[l]
            l, r = l+1, r-1
        return ''.join(ls)