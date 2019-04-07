class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or not s.replace(' ', ''):
            return 0
        if ' ' not in s:
            return len(s)
        return len(s.split()[-1])


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord(' '))
    print(sol.lengthOfLastWord(''))
    print(sol.lengthOfLastWord('    '))
    print(sol.lengthOfLastWord('aaaa '))
    print(sol.lengthOfLastWord('aaaa bbb'))
