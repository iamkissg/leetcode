from typing import List
# from random import randint, choice
import random


def quick_sort(nums: List[int], key=lambda x,y: x<=y) -> List[int]:
    return quick_sort_recursively(nums, key)

def quick_sort_recursively(nums: List[int], key=lambda x,y: x<=y) -> List[int]:
    '''
    非原地快排
    '''
    if len(nums) <= 1:
        return nums
    
    pivot_index = random.randint(0, len(nums)-1)
    pivot = nums[pivot_index]
    le_pivot = [a for a in nums[:pivot_index]+nums[pivot_index+1:] if key(a, pivot)]
    gt_pivot = [a for a in nums[:pivot_index]+nums[pivot_index+1:] if not key(a, pivot)]
    return quick_sort(le_pivot, key) + [pivot] + quick_sort(gt_pivot, key)

def quick_sort_inplace(nums, l, r):
    '''
    原地排序版, 一般需要这个版本吧
    '''
    if l < r:
        q = partition(nums, l, r)
        quick_sort_inplace(nums, l, q-1)
        quick_sort_inplace(nums, q+1, r)

def partition(nums, l, r):
    pivot = nums[r]
    i = l
    for j in range(l, r):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[r] = nums[r], nums[i]
    return i

if __name__ == "__main__":
    # print(quick_sort_in_place([3, 35,24,4]))
    # print(quick_sort_in_place([435,24,4,534,52,32,5,5647,6878798,7,5,3,1314,4], key=lambda x,y: x>=y))

    nums = [435,24,4,534,52,32,5,5647,6878798,7,5,3,1314,4]
    quick_sort_inplace(nums, 0, len(nums)-1)
    print(nums)