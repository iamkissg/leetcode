from string import printable

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        20191002
        执行用时 :44 ms, 在所有 Python3 提交中击败了88.92% 的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了5.88%的用户
        '''
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        if len(haystack) == len(needle):
            return 0 if haystack == needle else -1
        
        len_needle = len(needle)
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len_needle] == needle:
                return i
        else:
            return -1

    def KMP(self, pat):
        m = len(pat)
        # dp[状态][字符] = 下个状态
        dp = [{c: 0 for c in printable} for i in range(m)]
        dp[0][pat[0]] = 1

        X = 0
        for i in range(1, m):
            for c in printable:
                # # 状态匹配, 推进到下一个状态
                # if pat[i] == c:
                #     dp[i][c] = i+1
                # # 状态不匹配, 回退
                # else:
                #     dp[i][c] = dp[X][c]
                dp[i][c] = dp[X][c]
            dp[i][pat[i]] = i + 1
            X = dp[X][pat[i]]

        return dp


    def strStr_KMP(self, haystack: str, needle: str) -> int:
        '''
        20191002
        564 ms	163.7 MB	Python3
        484 ms	163.5 MB	Python3

        效率上有点出乎意料, 估计是构造 dp
        '''
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1

        m, n = len(needle), len(haystack)
        dp = self.KMP(needle)

        j = 0
        for i in range(n):
            j = dp[j][haystack[i]]
            if j == m:
                return i-m+1
        else:
            return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr('hello', 'll'))
    print(sol.strStr('hello', ''))
    print(sol.strStr('hello', 'h'))
    print(sol.strStr('hello', 'o'))
    print(sol.strStr('aaaaaa', 'ba'))
    print(sol.strStr('a', 'a'))
    print(sol.strStr('mississippi', 'pi'))
    print('#'*28)
    print(sol.strStr_KMP('hello', 'll'))
    print(sol.strStr_KMP('hello', ''))
    print(sol.strStr_KMP('hello', 'h'))
    print(sol.strStr_KMP('hello', 'o'))
    print(sol.strStr_KMP('aaaaaa', 'ba'))
    print(sol.strStr_KMP('a', 'a'))
    print(sol.strStr_KMP('mississippi', 'pi'))