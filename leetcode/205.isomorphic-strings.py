class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        
        d = {}
        used_values = set()
        for a, b in zip(s, t):
            if a not in d:
                if b in used_values:
                    return False
                d[a] = b
                used_values.add(b)
            elif d[a] != b:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isIsomorphic('ab', 'aa'))