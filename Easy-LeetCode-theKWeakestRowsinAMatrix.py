mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
def kWeakestRows(mat, k):
    dict_array = {}
    for i in mat: 
        for k, j in enumerate(i):
            Answer = j.count(1)
            dict_array[k] = Answer
    print (dict_array)
    

Answer = kWeakestRows(mat,3)
print (Answer)
