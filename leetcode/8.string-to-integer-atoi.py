class Solution:
    INT_MAX = (1 << 31) -1
    INT_MIN = -1<< 31
    sign = {'+', '-'}
    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    def myAtoi(self, s: str) -> int:
        '''
        20190928
        执行用时 :64 ms, 在所有 Python3 提交中击败了33.43% 的用户
        内存消耗 :14 MB, 在所有 Python3 提交中击败了5.16%的用户

        按部就班地算
        '''

        i = 0
        lens = len(s)
        nums = None
        while i < lens:
            if s[i] == ' ':
                i += 1
                continue
            elif s[i] in self.sign:
                is_negative = s[i] == '-'
                nums = self.find_nums(s[i+1:])
                break
            elif s[i] not in self.digits:
                return 0
            else:
                is_negative = False
                nums = self.find_nums(s[i:])
                break

        if not nums:
            return 0

        result = 0
        for c in nums:
            result = result * 10 + int(c)
        result = -result if is_negative else result
        if result < self.INT_MIN:
            result = self.INT_MIN
        elif result > self.INT_MAX:
            result = self.INT_MAX

        return result

    def find_nums(self, s: str):
        result = ''
        for c in s:
            if c in self.digits:
                result += c
            else:
                break
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi(''))
    print(sol.myAtoi('-'))
    print(sol.myAtoi('-0'))
    print(sol.myAtoi('42'))
    print(sol.myAtoi("   -42"))
    print(sol.myAtoi("4193 with words"))
    print(sol.myAtoi("words and 987"))
    print(sol.myAtoi("-91283472332"))
    print(sol.myAtoi("2147483646"))