from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        20190924
        我对动态规划, 真是没半点直觉啊
        '''

        max_money = [0, nums[0]]
        for i, n in enumerate(nums[1:], start=2):
            # print(max_money)
            max_money.append(max([max_money[i-1], max_money[i-2]+n]))
        
        return max_money[-1]



if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([2, 1, 1, 2]))