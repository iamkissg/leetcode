from typing import List
from math import cos

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        
        sc = sorted(coordinates, key=lambda t: t[0])
        n = len(sc)

        a, b, c = sc[0], sc[1], sc[2]
        step_x_1 = b[0]-a[0]
        step_y_1 = b[1]-a[1]
        step_x_2 = c[0]-b[0]
        step_y_2 = c[1]-b[1]
        if step_x_1 == 0 and step_x_2 == 0:
            for i in range(3, n):
                pre = sc[i-1]
                cur = sc[i]
                if pre[0]+step_x_1 != cur[0]:
                    return False
            return True
        elif step_y_1 == 0 and step_y_2 == 0:
            for i in range(3, n):
                pre = sc[i-1]
                cur = sc[i]
                if pre[1] + step_y_1 != cur[1]:
                    return False
            return True
        elif (step_x_1 == 0 and step_x_2 != 0) or (step_x_1 != 0 and step_x_2 == 0):
            return False
        elif (step_y_1 == 0 and step_y_2 != 0) or (step_y_1 != 0 and step_y_2 == 0):
            return False
        
        step_x_1, step_y_1 = step_x_1/step_x_1, step_y_1/step_x_1
        step_x_2, step_y_2 = step_x_2/step_x_2, step_y_2/step_x_2
        if step_x_2 != step_x_1 and step_y_2 != step_y_1:
            return False
        else:
            for i in range(3, n):
                pre = sc[i-1]
                cur = sc[i]
                
                try:
                    step_x_cur = (cur[0]-pre[0])
                    step_x_cur, step_y_cur = step_x_cur/step_x_cur, (cur[1]-pre[1])/step_x_cur
                    if step_x_cur != step_x_1 or step_y_cur != step_y_1:
                        return False
                except ZeroDivisionError:
                    return False
            return True

        
if __name__ == "__main__":
    sol = Solution()
    # print(sol.checkStraightLine([[-3,-2],[-1,-2],[2,-1],[-2,-2],[0,-2]]))
    # print(sol.checkStraightLine([[0,1],[1,3],[-4,-7],[5,11]]))
    print(sol.checkStraightLine([[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]))