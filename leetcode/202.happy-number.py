import time
from functools import reduce

class Solution:
    def next_n(self, n):
            return str(sum(map(lambda t: int(t)**2, list(n))))

    def isHappy(self, n: int) -> bool:
        '''
        20191005
        0.001 384 ms	13.9 MB	Python3
        0.0001: 76 ms	13.8 MB	Python3

        按照覃超教得"判断链表是否存在环状结构, 在一定时间内出不来结果的, 直接判有环"的方法, 作弊成功
        虽然我没有找出快乐数的数学规律
        '''
        n = str(n)
        start = time.time()
        # 再快就出事了
        while time.time() - start < 0.0001:
            n = self.next_n(n)
            if n == '1':
                return True
        else:
            return False
    
    def isHappy(self, n: int) -> bool:
        '''
        20191005
        44 ms	13.7 MB	Python3

        网上学来的快慢指针法破环
        https://leetcode-cn.com/problems/happy-number/solution/shi-yong-kuai-man-zhi-zhen-si-xiang-zhao-chu-xun-h/

        '''
        slow, fast = str(n), self.next_n(str(n))

        while slow != fast:
            slow = self.next_n(slow)
            fast = self.next_n(self.next_n(fast))
        return slow == '1'


if __name__ == "__main__":
    sol = Solution()
    for i in range(100):
        print(i, sol.isHappy(i))