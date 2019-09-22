from collections import deque
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        20190922
        解法来自 Leecode, https://leetcode.com/problems/ugly-number-ii/discuss/352644/Python-7-lines-O(N)-using-collections.deque
        发现挺神奇的, 就维护 3 个队列, 对应235, 然后每次取出全局最小的数 (需要从指定队列删除), 然后分别乘以235, 再加到队列尾部
        '''
        queues = {i: deque([1]) for i in [2, 3, 5]}

        for _ in range(n):
            result = min([q[0] for q in queues.values()])
            for i, q in queues.items():
                if result == q[0]:
                    q.popleft()
                q.append(result * i)
        return result

        



if __name__ == "__main__":
    sol = Solution()
    print(sol.nthUglyNumber(1))
    print(sol.nthUglyNumber(2))
    print(sol.nthUglyNumber(3))
    print(sol.nthUglyNumber(4))
    print(sol.nthUglyNumber(5))
    print(sol.nthUglyNumber(10))