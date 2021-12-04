# Input: x = 121
# Output: true

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# https://leetcode.com/problems/palindrome-number/
class Solution(object):

    def isPalindrome(self, x):
        x = list(str(x))
        middle = len(x) //2 
        for i, n in enumerate(x[:middle]):
            if x[i] != x[-(i+1)]:
                return False
        return True

                

        
        