class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True
        
        if len(s) % 2:
            return False

        if s[0] in {')', '}', ']'} or s[-1] in {'{', '(', '['}:
            return False

        valid_pairs = {'{}', '()', '[]'}

        stack = []
        for t in s:
            if t in {'(', '{', '['}:
                stack.append(t)
            elif t in{')', '}', ']'}:
                if stack[-1] + t in valid_pairs:
                    stack.pop()
                else:
                    return False
        else:
            return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid('()'))
    print(sol.isValid('()[]{}'))
    print(sol.isValid('(]'))
    print(sol.isValid('{[]}'))
    print(sol.isValid('{[]{'))
    print(sol.isValid('[]}'))