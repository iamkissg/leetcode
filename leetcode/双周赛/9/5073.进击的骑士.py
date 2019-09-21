# 超时
# 要动态规划的知识


from functools import cmp_to_key

up_down = [-2, -2, -1, -1, 1, 1, 2, 2]
left_right = [-1, 1, -2, 2, -2, 2, -1, 1]

class Solution:
    def __init__(self):
        self.steps = {(0, 0): 0}

    def minKnightMoves(self, x: int, y: int) -> int:
        if (x, y) in self.steps:
            return self.steps[(x, y)]

        passed = set()
        queue = [(0, 0)]

        while queue:
            a, b = queue.pop(0)

            if (a, b) in passed:
                continue
            passed.add((a, b))

            for i in range(8):
                na, nb = a+up_down[i], b+left_right[i]
                if abs(na-x)+abs(nb-y) > abs(a-x)+abs(b-y):
                    continue
                if (na, nb) in self.steps:
                    if (na, nb) not in passed:
                        queue.append((na, nb))
                    continue
                # 前面走不好了, 我们的 sort 会让走路不稳定, 可能一开始走了远路, 这时候要纠正
                # 但是怕就怕在连 ab 都是不好的
                # if (na, nb) in steps:
                #     if steps[(na, nb)] < steps[(a, b)] + 1:
                #     continue
                
                self.steps[(na, nb)] = self.steps[(a, b)] + 1
                if na == x and nb == y:
                    return self.steps[(na, nb)]

                queue.append((na, nb))
                # queue = sorted(
                #     queue,
                #     key=cmp_to_key(lambda p1, p2: (abs(p1[0]-x)+abs(p1[1]-y)-abs(p2[0]-x)-abs(p2[1]-y)) or (steps[p1]-steps[p2]))
                # )
                # print(queue)

if __name__ == "__main__":
    sol = Solution()
    print(sol.minKnightMoves(5, 5))
    # exit()
    print(sol.minKnightMoves(-34, -156))
    print(sol.minKnightMoves(34, -156))
    print(sol.minKnightMoves(34, 156))
    print(sol.minKnightMoves(-34, 156))
    print(sol.minKnightMoves(-34, -156))
    print(sol.minKnightMoves(34, -156))
    print(sol.minKnightMoves(34, 156))
    print(sol.minKnightMoves(-34, 156))
    print(sol.minKnightMoves(-34, -156))
    print(sol.minKnightMoves(34, -156))
    print(sol.minKnightMoves(34, 156))
    print(sol.minKnightMoves(-34, 156))