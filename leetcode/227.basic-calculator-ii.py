from math import copysign

class Solution:

    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []

        # opt 用于保存遇到下一个操作符之前的操作符, 对应于对前一个数字的操作, 挺秒的
        opt, num = '+', 0
        for i, c in enumerate(s):
            if c.isdigit():
                num = num*10+int(c)
            if c in {'+', '-', '*', '/'} or i == n-1:
                if opt == '-':
                    stack.append(-num)
                if opt == '+':
                    stack.append(num)
                if opt == '*':
                    stack.append(stack.pop()*num)
                elif opt == '/':
                    dividend = stack.pop()
                    stack.append(int(copysign(abs(dividend)//num, dividend)))
                    # if dividend < 0:
                    #     stack.append(-(-dividend//num))
                    # else:
                    #     stack.append(dividend//num)
                opt = c
                num = 0

        return sum(stack)

if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate("14-3/2"))
    print(sol.calculate(" 3/2 "))
    print(sol.calculate("3+2*2"))
    print(sol.calculate(" 3+5 / 2 "))
    print(sol.calculate("0/1"))