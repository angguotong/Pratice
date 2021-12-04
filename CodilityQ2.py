# A = "abcdezg"
# compare = list(A)
# new_list = []
# def solution (A, compare):
#     for i in range(len(compare)):
#         if i == len(A)-1: #this is to handle last character
#             compare.pop()
#             return "".join(compare)
#         elif compare[i] > compare[i + 1]:# this is to handle any other character
#             compare.pop(i)
#             return "".join(compare)

# answer = solution(A, compare)
# print (answer)


A = "abc"
compare = list(A)
new_list = []
def solution (A, compare):
    for i in range(len(compare)-1):
        if (compare[i] > compare[i + 1]):# this is to handle any other character
            compare.pop(i)
            return "".join(compare)
    return "".join(compare[:-1])

answer = solution(A, compare)
print (answer)