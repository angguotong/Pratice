A = [1,2,3,4,5]

Target = 3

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
        elif Target > A[midpoint]:
            left = midpoint + 1
    return -1 

Answer = BinarySearch(A, Target)
print (Answer)