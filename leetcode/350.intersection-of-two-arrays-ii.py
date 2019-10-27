from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        20191019

        和两个数组的交集 1 的做法类似, 采用了 set 来取交集, 但是用了 Counter 来统计不同 key 在两个数组中的次数
        """
        # 1. 计数法
        # 不同时间运行的, 差好大
        # 56 ms	14 MB	Python3
        # 92 ms	14 MB	Python3
        dict1 = Counter(nums1)
        dict2 = Counter(nums2)
        intersection_keys = dict1.keys() & dict2.keys()

        return [k for k in intersection_keys for i in range(min(dict1[k], dict2[k]))]

 

        # 2. 排序法
        # 依然差好大
        # 64 ms	13.7 MB	Python3
        # 92 ms	14 MB	Python3
        n, m = len(nums1), len(nums2)
        
        nums1.sort()
        nums2.sort()
        
        i1, i2 = 0, 0
        res = []
        while i1 < n and i2 < m:
            if nums1[i1] == nums2[i2]:
                res.append(nums1[i1])
                i1, i2 = i1+1, i2+1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
        return res