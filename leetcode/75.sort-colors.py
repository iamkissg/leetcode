from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
        20191022
        44 ms	13.8 MB	Python3

        按照题目的提示来, 统计每个数字的次数, 按序改变原数组, 遍历两次
        '''
        # if not nums:
        #     return []

        # d = defaultdict()
        # d.update({0: 0, 1: 0, 2: 0})
        # for a in nums:
        #     d[a] += 1

        # i = 0
        # for k, v in d.items():
        #     for j in range(v):
        #         nums[i] = k
        #         i += 1
    
        '''
        20191022
        五分钟学算法的一趟遍历法, 充分利用了题目信息:
        1. 3 个元素, 则用两个指针来维护三块区域, zero, two, 分别表征当前零区和二区的边界
        2. 用第三个指针来遍历数组
            1. 遇到 1, 不做任何处理, 遍历指针后移
            2. 遇到 0, 相当于当前元素要加入到零区, 先后移零指针, 然后交换, 遍历指针后移
            3. 遇到 2, 相当于当前元素要加入到二区, 先前移二指针, 然后交换, 此时不知道交换过来的元素是 1 还是 2, 遍历指针暂不后移
                1. 是 1, 按第一步走
                2. 是 2, 还得按第三步走
        '''
        if not nums:
            return []
        
        n = len(nums)
        zero, two = -1, n
        i = 0
        while i < two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i], nums[two] = nums[two], nums[i]