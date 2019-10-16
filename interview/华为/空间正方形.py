from itertools import combinations


class Solution(object):
    def euclidean_distance_2(self, p1, p2):
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if len(set(map(tuple, [p1, p2, p3, p4]))) < 4:
            return 0

        distances = [
            self.euclidean_distance_2(x, y)
            for x, y in combinations([p1, p2, p3, p4], 2)
        ]
        distances.sort()
        shorts = distances[:4]
        longs = distances[-2:]
        return len(set(shorts)) == 1 and len(set(longs))


if __name__ == "__main__":
    sol = Solution()
    print(sol.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))