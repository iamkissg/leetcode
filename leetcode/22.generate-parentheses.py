from typing import List
from queue import deque


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        20171007

        52 ms	14.3 MB	Python3
        采用 BFS, 检查剩余可用的左右括号数,
        对于左括号, 只有还有的用, 都可以拼接到当前字符串; 
        对于右括号, 只有当剩余右括号数大于左括号数, 才能拼接到当前字符串中
        '''
        res = []
        myque = deque(['('])
        n2 = 2*n

        while myque:
            par = myque.popleft()
            if len(par) == n2:
                res.append(par)
                continue
            
            rest_n_left = n-par.count('(')
            rest_n_right = n-par.count(')')
            if rest_n_left > 0:
                myque.append(par+'(')
            if rest_n_right > rest_n_left:
                myque.append(par+')')
            
        return res

        

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
    # ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    print(sol.generateParenthesis(4))
    print(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
