import random


class Solution:
    '''
    20191010
    356 ms	18.9 MB	Python3
    '''

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        indexes = [i for i in range(self.n)]
        shuffled = []
        for i in range(self.n):
            index = random.choice(indexes)
            shuffled.append(self.nums[index])
            indexes.remove(index)
        return shuffled
        

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()