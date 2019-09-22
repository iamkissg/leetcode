from typing import List
from collections import deque

import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        '''
        20190922
        丑数2 的解法, 因为 n 和 k 都不大, 沿用解法没有问题
        '''
        queues = {i: deque([1]) for i in primes}

        for _ in range(n):
            result = min([q[0] for q in queues.values()])
            for i, q in queues.items():
                if result == q[0]:
                    q.popleft()
                q.append(result*i)
        return result


    def nthSuperUglyNumber_heap(self, n: int, primes: List[int]) -> int:
        '''
        20190922
        不小心瞄到了丑数的讨论里有同学提到最小堆, 就实现了一下
        1200 ms	112.9 MB	Python  # 维护 visisted
        1304 ms	116.9 MB	Python3 # 不维护 visited, 只是将重复元素一直 pop 掉
        但是 Python 的 heapq 只能处理 List, 处理堆中的重复元素要稍微注意一下
        '''
        if n == 1:
            return 1

        min_heap = primes[:]
        heapq.heapify(min_heap)

        for _ in range(1, n):
            result = heapq.heappop(min_heap)
            while min_heap and min_heap[0] == result:
                heapq.heappop(min_heap)
            if result > 1:
                for p in primes:
                    heapq.heappush(min_heap, p*result)
        return result



if __name__ == "__main__":
    sol = Solution()
    print(sol.nthSuperUglyNumber(n = 12, primes = [2,7,13,19]))
    print(sol.nthSuperUglyNumber_heap(n = 12, primes = [2,7,13,19]))
    print(sol.nthSuperUglyNumber_heap(n = 2, primes = [2]))
