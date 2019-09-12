from math import log, floor, sqrt, ceil
import sys

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

    # Function to get minimum number of trials needed in worst 
    # case with n eggs and k floors 
    def superEggDrop(self, n, k): 
        
        # A 2D table where entery eggFloor[i][j] will represent minimum 
        # number of trials needed for i eggs and j floors. 
        eggFloor = [[0 for x in range(k+1)] for x in range(n+1)] 
    
        # We need one trial for one floor and0 trials for 0 floors 
        for i in range(1, n+1): 
            eggFloor[i][1] = 1
            eggFloor[i][0] = 0
    
        # We always need j trials for one egg and j floors. 
        for j in range(1, k+1): 
            eggFloor[1][j] = j 
    
        # Fill rest of the entries in table using optimal substructure 
        # property 
        for i in range(2, n+1): 
            for j in range(2, k+1): 
                eggFloor[i][j] = INT_MAX 
                for x in range(1, j+1): 
                    res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]) 
                    if res < eggFloor[i][j]: 
                        eggFloor[i][j] = res 
    
        # eggFloor[n][k] holds the result 
        return eggFloor[n][k] 



if __name__ == "__main__":
    sol = Solution()

    print(sol.superEggDrop(3, 14))
    print(sol.superEggDrop(1, 2))
    print(sol.superEggDrop(2, 6))
    print(sol.superEggDrop(2, 2))
    print(sol.superEggDrop(2, 4))