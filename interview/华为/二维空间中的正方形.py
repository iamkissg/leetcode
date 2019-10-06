from typing import List


class Solution:

    def euclidean_distance(self, p1, p2):
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = set([tuple(p) for p in [p1, p2, p3, p4]])
        if len(points) < 4:
            return False

        p0 = [(p1[0]+p2[0]+p3[0]+p4[0]) / 4, (p1[1]+p2[1]+p3[1]+p4[1]) / 4]

        dis_p0_p1 = self.euclidean_distance(p0, p1)
        dis_p0_p2 = self.euclidean_distance(p0, p2)
        dis_p0_p3 = self.euclidean_distance(p0, p3)
        dis_p0_p4 = self.euclidean_distance(p0, p4)

        if any([dis_p0_p2-dis_p0_p1, dis_p0_p3-dis_p0_p1, dis_p0_p4-dis_p0_p1]):
            return False

        dis_p1_p2 = self.euclidean_distance(p1, p2)
        dis_p1_p3 = self.euclidean_distance(p1, p3)
        dis_p1_p4 = self.euclidean_distance(p1, p4)
        if dis_p1_p2 == dis_p1_p3 or dis_p1_p2 == dis_p1_p4 or dis_p1_p3 == dis_p1_p4:
            return True
        else:
            return False

        print(dis_p0_p1, dis_p0_p2, dis_p0_p3, dis_p0_p3, dis_p0_p4)


if __name__ == "__main__":
    sol = Solution()
    print(sol.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))
    print(sol.validSquare([0,0],[5,0],[5,4],[0,4]))
    print(sol.validSquare([0,0],[0,0],[0,0],[0,0]))