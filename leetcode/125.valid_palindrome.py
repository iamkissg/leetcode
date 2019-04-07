class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        alphanumeric = '0123456789abcdefghijklmnopqrstuvwxyz'

        new_s = [t for t in s.lower() if t in alphanumeric]
        return new_s == new_s[::-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print(sol.isPalindrome(""))
    print(sol.isPalindrome("race a car"))