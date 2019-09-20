from string import digits


class Solution:
    def calculate(self, s: str) -> int:
        input_stack = []

        tmp = ''
        for c in s:
            if c == ' ':
                continue
            elif c != ')':
                input_stack.append(c)
            else:
                tmp_stack = []
                while True:
                    popped = input_stack.pop()
                    if popped == '(':
                        break
                    tmp_stack.append(popped)
                if '+' in tmp_stack:
                    input_stack.append(
                        str(int(''.join(tmp_stack[:tmp_stack.index('+')])) + \
                            int(''.join(tmp_stack[tmp_stack.index('+')+1:])))
                    )
                elif '-' in tmp_stack:
                    input_stack.append(
                        str(int(''.join(tmp_stack[:tmp_stack.index('+')])) - \
                            int(''.join(tmp_stack[tmp_stack.index('+')+1:])))
                    )
                else:
                    input_stack.append(''.join(tmp_stack))
        
        print(input_stack)

if __name__ == "__main__":
    sol = Solution()
    print(sol.calculate("1 + 1"))
    print(sol.calculate(" 2-1 + 2 "))
    print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))
        

                