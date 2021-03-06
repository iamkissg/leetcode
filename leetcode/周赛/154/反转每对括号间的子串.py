class Solution:
    # def reverseParentheses(self, s: str) -> str:
        # p1 = 0
        # p2 = len(s)-1

        # while p1 < p2:
        #     if (s[p1] == '(' and s[p2] == ')') or (s[p1] == ')' and s[p2] == '('):
        #         s = s.replace(s[p1:p2+1], s[p1+1:p2][::-1])
        #         p1 = 0
        #         p2 = len(s)-1
        #     elif s[p1] not in {'(', ')'}:
        #         p1 += 1
        #     elif s[p2] not in {'(', ')'}:
        #         p2 -= 1
        # return s

    def reverseParentheses(self, s: str) -> str:
        '''
        20190928
        执行用时 :40 ms, 在所有 Python3 提交中击败了95.30% 的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了100.00%的用户

        如此写法, 真的太舒服了!
        '''
        result = ['']
        for i, c in enumerate(s):
            if c not in {'(', ')'}:
                result[-1] += c
            elif c == '(':
                result.append('')
            elif c == ')':
                popped = result.pop()
                result[-1] += popped[::-1]
        return result[0]
    
    def reverseParentheses_old(self, s: str) -> str:
        '''
        20190915
        60 ms	14 MB	Python3

        很复杂的解法
        '''
        sign = 0
        normal_stack = []
        reverse_stack = []

        for i, c in enumerate(s):
            if c == '(':
                sign += 1

            if c != ')':
                if sign & 1:
                    reverse_stack.append(c)
                else:
                    normal_stack.append(c)
            else:
                if sign & 1:
                    while True:
                        popped = reverse_stack.pop()
                        if popped == '(':
                            break
                        else:
                            normal_stack.append(popped)
                    sign -= 1
                else:
                    while True:
                        popped = normal_stack.pop()
                        if popped == '(':
                            break
                        else:
                            reverse_stack.append(popped)
                    sign -= 1
        return ''.join(normal_stack)
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseParentheses("(abcd)"))
    print(sol.reverseParentheses("(u(love)i)"))
    assert sol.reverseParentheses("(ed(et(oc))el)") == "leetcode"
    assert sol.reverseParentheses("(ed(et(oc))el)") == "leetcode"
    print(sol.reverseParentheses("(ed(et(oc))el)"))
    assert sol.reverseParentheses("a(bcdefghijkl(mno)p)q") == "apmnolkjihgfedcbq"
    print(sol.reverseParentheses("a(bcdefghijkl(mno)p)q"))
    print(sol.reverseParentheses("ta()usw((((a))))"))