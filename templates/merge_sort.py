from  typing import List


def merge_sort(nums: List[int], l: int, r: int) -> List[int]:

    if l < r:
        mid = l + (r-l) // 2
        merge_sort(nums, l, mid)
        merge_sort(nums, mid+1, r)
    
        merge(nums, l, mid, r)


def merge(nums: List[int], l: int, mid: int, r: int) -> List[int]:
    n_1 = mid - l + 1  # include mid
    n_2 = r - mid

    left = nums[l: mid+1]
    right = nums[mid+1: r+1]

    i, j, k = 0, 0, l
    while i < n_1 and j < n_2:
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < n_1:
        nums[k] = left[i]
        i += 1
        k += 1

    while j < n_2:
        nums[k] = right[j]
        j += 1
        k += 1


if __name__ == "__main__":
    nums = [435,24,4,534,52,32,5,5647,6878798,7,5,3,1314,4]
    print(nums)
    merge_sort(nums, 0, len(nums)-1)
    print(nums)