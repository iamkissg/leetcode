from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        20191019

        和两个数组的交集 1 的做法类似, 采用了 set 来取交集, 但是用了 Counter 来统计不同 key 在两个数组中的次数
        """
        dict1 = Counter(nums1)
        dict2 = Counter(nums2)
        intersection_keys = dict1.keys() & dict2.keys()

        return [k for k in intersection_keys for i in range(min(dict1[k], dict2[k]))]