class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for c in strs:
            sc = ''.join(sorted(c))
            if sc not in d:
                d[sc] = [c]
            else:
                d[sc].append(c)

        return d.values()