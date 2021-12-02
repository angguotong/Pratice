

# # https://leetcode.com/problems/roman-to-integer/


# class Solution(object):
#     def romanToInt(self, s):
#         dict_= {
#             "I":1,
#             "V":5,
#             "X":10,
#             "L":50,
#             "C":100,
#             "D":500,
#             "M":1000,
#             } 
#         lastAlpha = ""
#         Answer = 0
#         for i in s: 

#             if lastAlpha == "I" and i == "V":
#                 Answer += 4
#             elif lastAlpha == "I" and i == "X":
#                 Answer += 9
#             elif lastAlpha == "X" and i == "L":
#                 Answer += 40
#             elif lastAlpha == "X" and i == "C":
#                 Answer += 90
#             elif lastAlpha == "X" and i == "C":
#                 Answer += 400
#             elif lastAlpha == "X" and i == "C":
#                 Answer += 900

#             Answer = dict_[i].value()

                
        
A  = {
    "A": 1
}

print (A["A"])