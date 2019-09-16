class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True
        
        if len(s) & 1:
            return False

        if s[0] in {')', '}', ']'} or s[-1] in {'{', '(', '['}:
            return False

        valid_pairs = {'{}', '()', '[]'}

        stack = []
        for t in s:
            if t in {'(', '{', '['}:
                stack.append(t)
            elif t in {')', '}', ']'}:
                if stack[-1] + t in valid_pairs:
                    stack.pop()
                else:
                    return False
        else:
            return True

    def isValid2(self, s: str) -> bool:

        if not s:
            return True

        stack = []
        d = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c not in d:
                stack.append(c)
            else:
                if not stack or d[c] != stack.pop():
                    return False
        return not stack


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid(')'))
    print(sol.isValid('('))
    print(sol.isValid('()'))
    print(sol.isValid('()[]{}'))
    print(sol.isValid('(]'))
    print(sol.isValid('{[]}'))
    print(sol.isValid('{[]{'))
    print(sol.isValid('{[]'))
    print(sol.isValid('{[]}}'))
    print(sol.isValid('[]}'))