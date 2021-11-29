
A = [-1,2,3,123,123,12,3,1,1,23,12,3,4124,16234,1,0,-1,23,-123,-512,-12,-3,-123]

Target = 23

#quick sort function 

def Quicksort (A):
    
    if len(A) <= 1:
        return A
    else:
        pivot = A.pop() # take out the last numebr 

    greater = []
    lower = []
    
    for i in A: 
        if i > pivot: 
            greater.append(i)
        else:
            lower.append(i)

    return Quicksort(lower) + [pivot] + Quicksort(greater)


def BinarySearch(A, Target):
    print (A, Target)
    left = 0 
    right = len(A) - 1

    while left <= right: 
        midpoint = int((left + right)/2)
        if A[midpoint] == Target:
            return A[midpoint]
        elif midpoint < Target: 
            left = midpoint - 1
        elif A[midpoint] > Target:
            right = midpoint + 1
    return -1
        
Answer = BinarySearch(Quicksort(A), Target)

print (Answer)