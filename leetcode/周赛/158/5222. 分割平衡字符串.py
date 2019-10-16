class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = []
        sub = ''
        counter = {'L': 0, 'R': 0}
        for c in s:
            sub += c
            counter[c] += 1
            if counter['L'] == counter['R']:
                res.append(sub)
                sub = ''
                counter = {'L': 0, 'R': 0}

        return len(res)

if __name__ == "__main__":
    sol = Solution()
    print(sol.balancedStringSplit(s = ""))
    print(sol.balancedStringSplit(s = "RLRRLLRLRL"))
    print(sol.balancedStringSplit(s = "RLLLLRRRLR"))
    print(sol.balancedStringSplit(s = "LLLLRRRR"))