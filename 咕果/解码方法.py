class Solution:

    valid_nums = {str(i) for i in range(1, 27)}
    def is_valid(self, s):
        return s in self.valid_nums

    def numDecodings(self, s: str) -> int:
        '''
        20191005
        执行用时 :40 ms, 在所有 Python3 提交中击败了96.72% 的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.21%的用户

        根据递归+记忆化的思路, 可以改写成从右到左的递推形式, 尝试着改写, 一直错. 参考了网友的写法
        https://leetcode-cn.com/problems/decode-ways/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-2-3/
        比较难以想到的是, dp table 长度是 len(s)+1
        '''
        if s.startswith('0') or not s:
            return 0

        n = len(s)
        if n == 1:
            return 1

        dp = [0 for i in range(n+1)]
        dp[-1] = 1
        dp[-2] = 1 if s[-1] != '0' else 0

        for i in range(n-2, -1, -1):
            if s[i] == '0': continue
            
            dp[i] = dp[i+1]
            if self.is_valid(s[i:i+2]):
                dp[i] += dp[i+2]

        return dp[0]

    def numDecodings_dp(self, s: str) -> int:
        '''
        20191004
        48 ms	14.6 MB	Python3
        题解来自: https://www.youtube.com/watch?v=qli-JCrSwuk

        视频里很细致地对情况进行了拆解, 在我看过的视频里, 是讲解最清楚的, 代码写起来也很简洁, 而且用一个 k 来表示剩余子串长度, 算是学到一招
        该问题和斐波那契数列是挺相似的, 差别在于, 边界条件的处理上,
        1. 0 开头的是非法密文, 所以解码对应的明文数为 0
        2. 0 开头的情况被处理掉之后, 总是有 result=self.helper(s, k-1)
        3. 另有一种情况下, 前面两个数字对应一个明文, 此时对密文有特殊要求, 因此按条件追加
        '''
        self.memo = {}
        res = self.helper(s, len(s))
        return res

    def helper(self, s: str, k: int) -> int:
        if k == 0:
            return 1

        i = len(s) - k
        if s[i] == '0':
            return 0

        if (s, k) in self.memo:
            return self.memo[(s, k)]

        result = self.helper(s, k-1)
        if k >= 2 and int(s[i:i+2]) <= 26:
            result += self.helper(s, k-2)
        self.memo[(s, k)] = result
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("226"))
    print(sol.numDecodings(""))
    print(sol.numDecodings("1"))
    print(sol.numDecodings("12"))
    print(sol.numDecodings("100"))
    print(sol.numDecodings("110"))
    print(sol.numDecodings("101"))
    print(sol.numDecodings("28"))
    print(sol.numDecodings("26"))
    print(sol.numDecodings("230"))