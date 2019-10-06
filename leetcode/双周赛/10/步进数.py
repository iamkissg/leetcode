from typing import List
from queue import deque


class Solution:

    # def is_stepping_number(self, num):
    #     num = str(num)

    #     if len(num) == 1:
    #         return True

    #     for i in range(1, len(num)):
    #         if num[i-1] not in self.steps[num[i]]:
    #             return False
    #     return True


    # def countSteppingNumbers(self, low: int, high: int) -> List[int]:
    #     return list(map(int, filter(self.is_stepping_number, range(low, high+1))))

    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(10):
            res.extend(self.bfs(low, high, i))

        return sorted(map(int, res))

    steps = {
        "0": ["1"],
        "1": ["0", "2"],
        "2": ["1", "3"],
        "3": ["2", "4"],
        "4": ["3", "5"],
        "5": ["4", "6"],
        "6": ["5", "7"],
        "7": ["6", "8"],
        "8": ["7", "9"],
        "9": ["8"],
    }

    def bfs(self, low, high, num):
        num = str(num)
        myque = deque([num])

        res = []
        while myque:
            step_num = myque.popleft()
            int_step_num = int(step_num)

            if int_step_num == 0 or int_step_num > high:
                continue
            
            if low <= int_step_num <= high:
                res.append(step_num)
            
            end = step_num[-1]
            myque.append(step_num+self.steps[end][0])
            if end not in ("0", "9"):
                myque.append(step_num+self.steps[end][1])

        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.countSteppingNumbers(0, 10000000))
    print(sol.countSteppingNumbers(0, 21))