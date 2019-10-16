from math import log10, floor

class Solution(object):
    def isPalindrome(self, x):
        """
        20191015
        108 ms	14 MB	Python3

        总的来说, 不用字符串来求回文数, 会显得稍微繁琐点, 每次要取头和取尾
        取尾的操作很简单, 取余就行;
        取头的操作稍微复杂一些, 首先确定输入 x 的位数, 即最高位对应 10 的多少次方, 然后取头就变成了 x//m
        x 和 m 更新操作, 可能要稍微控制下, 以及循环结束条件
        """
        if x < 0:
            return False
        if x < 10:
            return True
        # str_x = str(x)
        # return str_x == str_x[::-1]

        # 计算 x 的位数
        m = 1
        # 用出发会出错, 需用整除
        while x // m > 9:
            m *= 10
        
        while x > 0:
            head = x // m
            tail = x % 10
            if head != tail: return False
            x = (x%m) // 10
            m //= 100

        else:
            return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(44))
    print(sol.isPalindrome(1021))
    print(sol.isPalindrome(323))
    print(sol.isPalindrome(12))
    print(sol.isPalindrome(999))
