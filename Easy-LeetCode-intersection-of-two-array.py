# https://leetcode.com/problems/intersection-of-two-arrays/



class Solution(object):
    def intersection(self, nums1, nums2):        

        set1 = set(nums1)
        set2 = set(nums2)
        answer = []

        for i in set1: 
            if i in set2: 
                answer.append(i)
        return answer