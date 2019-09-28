from typing import List


class Solution:
    def expand(self, S: str) -> List[str]:
        '''
        20190928
        执行用时 :52 ms, 在所有 Python3 提交中击败了85.71% 的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了100.00%的用户
        '''
        result = ['']
        i = 0
        while i < len(S):
            if S[i] not in {'{', '}'}:
                result = [res+S[i] for res in result]
            elif S[i] == '{':
                j = S[i:].find('}')
                s = S[i+1: i+j].split(',')
                result = [res+c for c in s for res in result]
                i += j
            i += 1
        return sorted(result)



if __name__ == "__main__":
    sol = Solution()
    print(sol.expand('{a,b}c{d,e}f'))
    print(sol.expand("abcd"))
    print(sol.expand(""))