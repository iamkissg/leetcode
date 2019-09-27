from typing import List


class Solution:

    def minCost(self, costs: List[List[int]]) -> int:
        return self.minCost_DP(costs)

    def minCost_DP(self, costs: List[List[int]]) -> int:
        '''
        20190925
        我大概是猪吧, 状态转移方程怎么都找不出来, 感觉这是一道困难题
        看了网友的题解, 真是简单啊
        '''
        if not costs:
            return 0

        R, G, B = 0, 0, 0
        for r, g, b in costs:
            R, G, B = r+min(G, B), g+min(R, B), b+min(G, R)
        return min([R, G, B])


    # def minCost(self, costs: List[List[int]]) -> int:
    #     if not costs:
    #         return 0

    #     my_costs = [[(c, i) for i, c in enumerate(costs[0])]]

    #     for cost in costs[1:]:
    #         next_cost = []
    #         for c, i in my_costs[-1]:
    #             min_next_cost = min([nc for j, nc in enumerate(cost) if j!=i])
    #             index_min_next_cost = cost.index(min_next_cost)
    #             next_cost.append((c+min_next_cost, index_min_next_cost))

    #             # next_cost.append((my_costs[-1][i]+min([c for j,c in enumerate(cost) if j!=i]), ))

    #         my_costs.append(next_cost)

    #     return min(my_costs[-1])


if __name__ == "__main__":
    sol = Solution()
    print(sol.minCost([[17,2,17],[16,16,5],[14,3,19]]))
    print(sol.minCost([[17,15,10],[16,2,17],[14,8,15],[5,4,15],[16,1,2],[8,20,1]]))
    # print(sol.minCost([[17,15,10],[16,2,17],[14,8,15],[5,4,15],[16,1,2],[8,20,1],[15,20,16],[7,3,14],[1,14,15],[17,3,11],[16,12,18],[12,20,16],[20,2,10],[19,13,10],[1,18,8]]))


