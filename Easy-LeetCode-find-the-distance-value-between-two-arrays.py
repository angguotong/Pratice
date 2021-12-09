# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/submissions/



class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        
        counter = 0        
        for i in arr1: 
            for j in arr2:                 
                if abs(i-j) <= d:
                    counter += 1
                    break        
        return (len(arr1) - counter )
    
