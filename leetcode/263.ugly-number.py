class Solution:
    def isUgly(self, num: int) -> bool:
        '''
        20190922
        36 ms	13.9 MB	Python3
        '''
        # 根据题目要求, 丑数是正整数, 且 1 是丑数
        if num == 1:
            return True
        elif num < 1:
            return False

        # 从 2 开始, 不断尝试去整除当前数
        prime = [2, 3, 5]
        while num:
            if not num % prime[0]:
                # 模 0 说明整除, 取整除的结果
                num = num // prime[0]
            else:
                # 模不为 0, 替换下一个数字
                # 也可能, 已经整除至 1 了, 说明是丑数; 235都除不尽, 不是丑数
                if num == 1:
                    return True
                if len(prime) == 1:
                    return False
                prime.pop(0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.isUgly(-1))
    print(sol.isUgly(0))
    print(sol.isUgly(1))
    print(sol.isUgly(9))
    print(sol.isUgly(14))
    print(sol.isUgly(18))
        