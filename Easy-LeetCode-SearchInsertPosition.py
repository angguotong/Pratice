# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# https://leetcode.com/problems/search-insert-position/

A = [1,3,4,12,13]

Target = 2


def searchInsert(nums, target):
    if target not in nums: 
        nums.append(target)
    nums = sorted(nums)

    left = 0
    right = len(nums)-1

    while left <= right:
        midpoint = int((left + right)/2)
        if nums[midpoint] == target: 
            return midpoint
        elif target < nums[midpoint]:
            right = midpoint - 1
        elif target > nums[midpoint]:
            left = midpoint + 1
    return -1


