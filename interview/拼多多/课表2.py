from typing import List
from  queue import deque
from itertools import combinations


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        20191004
        176 ms	15.4 MB	Python3

        按照 leetcode 上网友的模板写的代码, 拓扑排序的通用模板
        1. 构造两个字典, 一个存储拓扑结构, 一个存储节点的入度
        2. 从图中入度为 0 的节点 (没有任何铺垫课程) 开始, 将它从拓扑结构中去除, 它的所有子节点的入度 -1
            1. 为了不破坏图结构, 我们使用前面构造的入度字典
        3. 如果不存在入度为 0 的节点, 说明节点之间存在环状结构, 不可能实现课程学习
        '''
        course_ids = [i for i in range(numCourses)]
        if not prerequisites:
            return course_ids

        # 1. 初始化两个字典, 一个存储节点入度, 一个存储拓扑结构
        in_degree = {cid: 0 for cid in course_ids}
        topo_map = {cid: [] for cid in course_ids}

        # 2. 填充字典
        for cur, pre in prerequisites:
            # cur <- pre
            # 便于找到子节点, 然后子节点入度减一
            topo_map[pre].append(cur)
            in_degree[cur] += 1

        # 3. 寻找入度为 0 的节点, 将它的子节点的入度都剪一, 直到所有节点的入度都为 1
        res = []
        while in_degree:
            flag = False
            for k in in_degree.keys():
                if in_degree[k] == 0:
                    res.append(k)
                    for nxt in topo_map[k]:
                        in_degree[nxt] -= 1

                    in_degree.pop(k)
                    flag = True
                    break
            if not flag:
                return []

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print(sol.findOrder(2, [[1,0]]))
    print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2],[0,3]]))
    print(sol.findOrder(4, [[1,0],[3,2]]))
    print(sol.findOrder(4, [[3,0],[0,1]]))
    print(sol.findOrder(2, []))
    print(sol.findOrder(1, []))
    print(sol.findOrder(3, [[0,2],[1,2],[2,0]]))