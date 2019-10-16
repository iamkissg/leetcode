from typing import List


# class Solution:
#     def __init__(self):
#         self.MOD = 10**9+7

#     def dieSimulator(self, n: int, rollMax: List[int]) -> int:
#         if n == 0:
#             print('Holly Shit')
#             return 0
#         if n == 1:
#             return len([rmx for rmx in rollMax if rmx > 0])

#         res = 0
#         for i in range(6):
#             if rollMax[i] > 0:
#                 # print(n-1, tmp, self.dieSimulator(n-1, tmp))
#                 tmp = rollMax[:]
#                 tmp[i] -= 1
#                 res = (res + self.dieSimulator(n-1, tmp)) % self.MOD

#         return res

class Solution(object):
    def dieSimulator(self, n, rollMax):
        '''
        排行榜上的解
        '''
        mod = 10 ** 9 + 7
        pre = [[0] * 16 for _ in range(6)]
        for i in range(6):
            pre[i][1] = 1

        for i in range(2, n+1):
            now = [[0] * 16 for _ in range(6)]
            for i in range(6):
                for j in range(1, 16):
                    if j + 1 <= rollMax[i]:
                        now[i][j+1] += pre[i][j]
                        now[i][j+1] = now[i][j+1] % mod
                    for k in range(6):
                        if k != i:
                            now[k][1] += pre[i][j]
                            now[k][1] = now[k][1] % mod
            pre = now
        for p in pre:
            print(p)
        return sum([sum(p)%mod for p in pre])%mod
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.dieSimulator(2, [0, 1, 1, 2, 2, 3]))
    print(sol.dieSimulator(2, [1, 0, 1, 2, 2, 3]))
    print(sol.dieSimulator(2, [1, 1, 0, 2, 2, 3]))
    print(sol.dieSimulator(2, [1, 1, 1, 1, 2, 3]))
    print(sol.dieSimulator(2, [1, 1, 1, 2, 1, 3]))
    print(sol.dieSimulator(2, [1, 1, 1, 2, 2, 2]))
    print(sol.dieSimulator(n = 3, rollMax = [1,1,1,2,2,3]))
    # print(sol.dieSimulator(n = 2, rollMax = [1,1,2,2,2,3]))
    # print(sol.dieSimulator(n = 2, rollMax = [1,1,1,1,2,3]))
    # print(sol.dieSimulator(n = 2, rollMax = [1,1,1,1,1,1]))
    # print(sol.dieSimulator(n = 1, rollMax = [1,1,0,1,1,1]))