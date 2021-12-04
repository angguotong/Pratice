#given a set of integers, you need to find the contuous subset of set whose sum is equal to k
# 2 4 1 5 6
# k=10

Array = [2,4,1,5,6]
Target = 10 



# Q1, Adding all


Answer = 0
for i in Array:
    Answer += i
    if Answer == Target: 
        print (True)
        break



# Q2, Adding not from start

for i in range(len(Array)):
    Answer = 0
    for j in Array[i:]:
        Answer += j
        if Answer == Target:
            print (True)
            break 
