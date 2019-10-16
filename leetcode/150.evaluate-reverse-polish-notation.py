from typing import List


class Solution:
    opts = {'+', '-', '*', '/'}

    def evalRPN(self, tokens: List[str]) -> int:

        res = []
        for c in tokens:
            if c not in self.opts:
                res.append(int(c))
            else:
                b = res.pop()
                a = res.pop()
                if c == '+': res.append(a+b)
                if c == '-': res.append(a-b)
                if c == '*': res.append(a*b)
                if c == '/':
                    if (a > 0 and b > 0) or (a < 0 and b < 0):
                        res.append(a//b)
                    else:
                        res.append(-(abs(a)//abs(b)))

        return res[0]

if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
    print(sol.evalRPN(["2", "1", "+", "3", "*"]))
    print(sol.evalRPN(["4", "13", "5", "/", "+"]))