class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        20191023
        80 ms	14.3 MB	Python3

        有没有序对于两数之和似乎没啥关系
        '''
        # d = {}
        # for i, a in enumerate(numbers):
        #     b = target-a
        #     if b in d:
        #         return d[b]+1, i+1
        #     else:
        #         d[a] = i

        # 两头往中间凑法
        l, r = 0, len(numbers) - 1
        while l < r:
            summed = numbers[l] + numbers[r]
            if summed < target:
                l += 1
            elif summed > target:
                r -= 1
            else:
                return l+1, r+1