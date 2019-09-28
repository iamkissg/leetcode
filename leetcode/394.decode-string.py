from string import digits, ascii_letters


class Solution:
    def decodeString(self, s: str) -> str:
        '''
        20190928
        执行用时 :32 ms, 在所有 Python3 提交中击败了99.61% 的用户
        内存消耗 :13.6 MB, 在所有 Python3 提交中击败了5.26%的用户

        思路借鉴了第 154 场周赛, 一位小哥的解法. 维护了一个栈, 最终结果保存在栈底元素中
        1. 每当遇到括号需要进行操作时, 都向栈中压入一个空串,
        2. 在操作完成之后, 将处理后的字符串 pop 出来, 拼接到栈顶的字符串中
        3. 重复 1, 2 步, 最终栈中只有一个元素, 即处理完的字符串
        '''
        result = ['']
        counts = []

        i = 0
        while i < len(s):
            if s[i] in ascii_letters:
                result[-1] += s[i]
            elif s[i] in digits:
                j = s[i:].find('[')
                counts.append(int(s[i: i+j]))
                result.append('')
                i += j
            elif s[i] == ']':
                count = counts.pop()
                sub_str = result.pop()
                result[-1] += sub_str * count
            i += 1
        return result[0]

    def decodeString_recursively(self, s: str) -> str:
        '''
        20190928
        尝试使用深度优先遍历的递归写法
        无从下手, 参考了比较多网友的写法, 以 '[' 作为递归的开始, ']' 作为递归的结束
        如此就能对一组"密码"进行解码, 后面的操作就容易了

        执行用时 :40 ms, 在所有 Python3 提交中击败了94.53% 的用户
        内存消耗 :13.7 MB, 在所有 Python3 提交中击败了5.26%的用户
        '''
        def dfs(string, i):
            result = ''
            count = 0
            while i < len(string):
                if string[i] in ascii_letters:
                    result += string[i]
                elif string[i] in digits:
                    count = count * 10 + int(string[i])
                elif string[i] == '[':
                    sub_str, i = dfs(string, i+1)
                    result += sub_str * count
                    count = 0
                elif string[i] == ']':
                    return result, i
                i += 1
            return result

        return dfs(s, 0)


if __name__ == "__main__":
    sol = Solution()
    # print(sol.decodeString(''))
    # print(sol.decodeString('3[a]2[bc]'))
    # print(sol.decodeString("3[a2[c]]"))
    # print(sol.decodeString("2[abc]3[cd]ef"))
    print(sol.decodeString_recursively(''))
    print(sol.decodeString_recursively('3[a]2[bc]'))
    print(sol.decodeString_recursively("3[a2[c]]"))
    print(sol.decodeString_recursively("2[abc]3[cd]ef"))