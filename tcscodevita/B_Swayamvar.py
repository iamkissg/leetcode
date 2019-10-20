import sys
from queue import deque


class Solution:
    def match(self, brides, grooms) -> int:
        count = 0
        while brides:
            b = brides.popleft()
            g = grooms.popleft()
            count = 0
            while b != g:
                grooms.append(g)
                count += 1
                if count == len(grooms):
                    return len(grooms)
                g = grooms.popleft()
        return 0


if __name__ == "__main__":
    sol = Solution()
    N = int(input())
    brides = deque(input())
    grooms = deque(input())
    print(sol.match(brides, grooms), end='')