from typing import List


class Solution:

    def overlapping_interval(self, a, b):
        return [max(a[0], b[0]), min(a[1], b[1])]

    def is_overlapped(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        slots1 = sorted(slots1, key=lambda t: t[0])
        slots2 = sorted(slots2, key=lambda t: t[0])

        n, m = len(slots1), len(slots2)
        i, j = 0, 0
        while i < n and j < m:
            a, b = slots1[i], slots2[j]
            if self.is_overlapped(a, b):
                interval = self.overlapping_interval(a, b)
                if interval[1] - interval[0] >= duration:
                    return [interval[0], interval[0]+duration]
            if a[1] <= b[1]:
                i += 1
            else:
                j += 1
        else:
            return []


if __name__ == "__main__":
    sol = Solution()
    # print(sol.minAvailableDuration([[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8))
    # print(sol.minAvailableDuration([[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12))
    print(sol.minAvailableDuration([[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]],
          [[50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]],
          456085))
