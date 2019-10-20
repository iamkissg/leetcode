from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        '''
        20191020

        网友的神奇`桶解法`
        https://leetcode-cn.com/problems/contains-duplicate-iii/solution/li-yong-tong-de-yuan-li-onpython3-by-zhou-pen-chen/

        要求差值不大于 t, 于是以 t+1 作为桶的大小,
        1. 于是在不大于 k 的窗口中, 有两个元素落在同一个桶中, 返回 True
        2. 相邻桶非空, 且和相邻桶中元素的差值不大于 t, 返回 True

        维护一个窗口大小为 k 的滑动窗口, 只需要 `i>=k, delete no.(i-k) element` 即可
        "桶"具体用字典来实现
        这解法太神奇了
        '''
        if not nums:
            return False
        if t < 0 or k < 0:
            return False
        
        n = len(nums)
        buckets = {}
        bucket_size = t + 1
        for i in range(n):
            bucket_index = nums[i] // bucket_size

            if bucket_index in buckets:
                return True

            print(nums[i])
            buckets[bucket_index] = nums[i]

            if (bucket_index-1) in buckets and abs(buckets[bucket_index-1]-nums[i]) <= t:
                return True
            if (bucket_index+1) in buckets and abs(buckets[bucket_index+1]-nums[i]) <= t:
                return True
            
            if i >= k:
                buckets.pop(nums[i-k]//bucket_size)
        return False
            


        # 以下设计重复计算, 超时了
        # l = 0
        # for r in range(1, n):
        #     while r - l > k:
        #         l += 1
            
        #     for i in range(l, r):
        #         if -t<=nums[r]-nums[i]<=t:
        #             return True
        # return False


if __name__ == "__main__":
    sol = Solution()

    print(sol.containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0))
    print(sol.containsNearbyAlmostDuplicate(nums = [1,0,1,1], k = 1, t = 2))
    print(sol.containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3))
