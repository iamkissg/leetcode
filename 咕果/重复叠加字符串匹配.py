import re


class Solution:

    def repeatedStringMatch(self, A: str, B: str) -> int:
        '''
        20191002
        执行用时 :132 ms, 在所有 Python3 提交中击败了82.07% 的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.81%的用户

        网友的神奇解法, 通过长度, 确定B基本由多少个A重叠而成, 最多的情况就是, 后缀+N个A+前缀, 所以考虑最多加两个A即可.
        '''
        count = len(B)//len(A)
        A_new = A*count
        if B in A_new: return count
        if B in A_new+A: return count+1
        if B in A_new+A+A: return count+2
        return -1

    # def repeatedStringMatch(self, A: str, B: str) -> int:
        '''
        20191002
        我大概是傻逼, 以下写得是什么垃圾代码???
        '''
        # len_A, len_B = len(A), len(B)

        # if B in A:
        #     return 1
        
        # count = len(re.findall(A, B))
        # if count:
        #     try:
        #         lB, rB = B.split(A*count)
        #     except ValueError:
        #         return -1
        # else:
        #     for i in range(len_A):
        #         if B in A[i:]+A[:i]:
        #             return 2
        #     else:
        #         return -1

        # if not lB and not rB:
        #     return count
        
        # if not lB:
        #     return count + 1 if A.startswith(rB) else -1
        # if not rB:
        #     return count + 1 if A.endswith(lB) else -1
        # return count + 2 if A.startswith(rB) and A.endswith(lB) else -1
        
        


if __name__ == "__main__":
    sol = Solution()
    # assert sol.repeatedStringMatch("abcd", "abcdb") == -1
    # assert sol.repeatedStringMatch("abc", "cabcabca") == 4
    # assert sol.repeatedStringMatch(A="a", B="aa") == 2
    # assert sol.repeatedStringMatch("bb", "bbbbbbb") == 4
    # assert sol.repeatedStringMatch(A="abcd", B="ab") == 1
    # assert sol.repeatedStringMatch(A="abcd", B="cdab") == 2
    # assert sol.repeatedStringMatch(A="abcd", B="cdabcdab") == 3
    # assert sol.repeatedStringMatch(A="abcd", B="cdabcdabcdab") == 4
    # print(sol.repeatedStringMatch("abc", "aabcbabcc"))
    # print(sol.repeatedStringMatch("abc", "abcabcc"))
    print(sol.repeatedStringMatch("abcd", "bcdab"))