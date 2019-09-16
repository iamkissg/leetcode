from string import ascii_lowercase, ascii_uppercase, digits

alphabet_digits = ascii_lowercase+ascii_uppercase+digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True

        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            if s[p1] not in alphabet_digits:
                p1 += 1
                continue
            if s[p2] not in alphabet_digits:
                p2 -= 1
                continue
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome('1'))
    print(sol.isPalindrome(''))
    print(sol.isPalindrome('11'))
    print(sol.isPalindrome('111'))
    print(sol.isPalindrome('113'))
    print(sol.isPalindrome('121'))
    print(sol.isPalindrome('1221'))
    print(sol.isPalindrome('"A man, a plan, a canal: Panama"'))
    print(sol.isPalindrome('"race a car"'))