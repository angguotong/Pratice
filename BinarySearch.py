A = [-1,0,1,3,4,5,6,7,8,9,10,11,12,13,14]

Target = 12

#binary sort to find the numebr

def BinarySearch (A, Target):

    left = 0 
    right = len(A) - 1 

    while left <= right: 
        midpoint = int((left + right)/2)
        if A[midpoint] == Target:
            return A[midpoint]
        elif Target < A[midpoint]:
            right = midpoint - 1
        elif Target > midpoint:
            left = midpoint + 1
    return -1 


Answer = BinarySearch(A, Target)
print (Answer)