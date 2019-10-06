from math import log, floor, sqrt, ceil
import sys

INT_MAX = sys.maxsize

class Solution:
    # def superEggDrop(self, K: int, N: int) -> int:
    #     if N == 1 or N == 0:
    #         return N

    #     if K == 1 and N:
    #         return N

    #     min = sys.maxsize
    
    #     # Consider all droppings from 1st  
    #     # floor to kth floor and return  
    #     # the minimum of these values plus 1. 
    #     for x in range(1, N + 1): 
    
    #         res = max(self.superEggDrop(K - 1, x - 1),
    #                   self.superEggDrop(K, N - x)) 
    #         if (res < min): 
    #             min = res 
    
    #     return min + 1

    def superEggDrop(self, K, N): 
        '''
        20191001
        第 15 次尝试, 终于成功了, 真不容易啊
        采用了 https://www.youtube.com/watch?v=xsOCvSiSrSs 的思路,
        和本地的 K 个鸡蛋, N 层楼, 确定最少所需的实验次数不同, 这个视频里提出了一个更一般性的方法: K 个鸡蛋, N 次实验, 最多能确定多少层楼 (为了区分, 以下称实验次数为 E 次)
        结论异常美: dp[E][K]=dp[E-1][K-1] + dp[E-1][K] + 1, 这个递推公式太好写了!!!
        两个 basecase: 只有 1 个鸡蛋, N 层楼必须实验 N 次; 只有一层楼, 只要有鸡蛋, 都只用实验 1 次
        这个递归公式要解释成: K 个鸡蛋, E 次实验, 最多可以确定的楼高.
        直观地理解是实验一次 dp[x][y], 分为两种情况:
        1. 鸡蛋碎了, 那么要用剩下的 y-1 个鸡蛋去检验 x-1 层, 为了使检验的楼层尽量高, 希望下面的楼层尽量高, 这是一个子问题: dp[x-1][y-1]
        2. 鸡蛋没碎, 那么有 y 个鸡蛋去检验后面的楼层, 向上和向下检验其实是类似的, 为了是楼层尽量高, 转为子问题 dp[x-1][y]
        dp[x][y] 能确定的楼层最高就是, 上面的楼层数+下面的楼层数+当前楼层, 所以 dp[x][y] = d[x-1][y-1] + d[x-1][y] + 1

        执行用时 :56 ms, 在所有 Python3 提交中击败了61.56% 的用户
        内存消耗 :13.9 MB, 在所有 Python3 提交中击败了44.57%的用户
        '''
        if N <= 1 or K == 1:
            return N

        # 二维数组用于保存 i 层, j 个鸡蛋的最优解 (问题转换得和最长递增子序列有点像)
        # N * K 的矩阵, 行表示层数, 列表示鸡蛋数
        dp = [[1 for _ in range(K)]]

        while dp[-1][K-1] < N:
            dp.append([len(dp)+1])
            cur_level = len(dp)-1
            for k in range(1, K):
                dp[cur_level].append(dp[cur_level-1][k-1] + dp[cur_level-1][k] + 1)

        return len(dp)

    # def superEggDrop(self, K, N):
    #     """
    #     :type K: int
    #     :type N: int
    #     :rtype: int
    #     """
    #     prev = [1] * K
    #     if K == 1:
    #         return N
    #     if N==0 or N == 1:
    #         return N

    #     for i in range(2, N+1):
    #         curr = [i]
    #         for j in range(1, K):
    #             curr.append(prev[j-1] + prev[j] + 1)
    #             print(curr)
    #             if curr[j] >= N:
    #                 return i
    #         prev = curr



    
        # # 1 层, 无论鸡蛋, 都只用试一次; 题目不会出现 0 层, 但是 0 层, 不用试, 所以设为 0
        # for k in range(K+1):
        #     eggFloor[1][k] = 1
        #     eggFloor[0][k] = 0
    
        # # 只有一个鸡蛋的情况下, 那就老实从下往上一层层地试
        # for n in range(N+1):
        #     eggFloor[n][0] = 0
        #     eggFloor[n][1] = n
        
        # # 填充 DP table
        # for k in range(2, K+1):
        #     for n in range(2, N+1):
        #         eggFloor[n][k] = eggFloor[n-1][k-1] + eggFloor[n-1][k] + 1
        #         # for x in range(1, n+1):
        #             # res = 1 + max(eggFloor[x-1][k-1], eggFloor[n-x][k])
        #             # if res < eggFloor[n][k]:
        #             #     eggFloor[n][k] = res
        # for n in range(N+1):
        #     if eggFloor[n][k] >= N:
        #         return n-1 if eggFloor[n][k] > N else n
    

if __name__ == "__main__":
    sol = Solution()

    print(sol.superEggDrop(3, 14))
    print(sol.superEggDrop(1, 2))
    print(sol.superEggDrop(2, 6))
    assert sol.superEggDrop(2, 2) == 2
    print(sol.superEggDrop(2, 4))
    print(sol.superEggDrop(2, 5000))