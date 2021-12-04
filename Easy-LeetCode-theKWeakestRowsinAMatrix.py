mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
def kWeakestRows(mat, k):
    dictionary = {}
    for i in mat: 
        for k, j in enumerate(i):
            Answer = j.count(1)
            dictionary[k] = Answer

    for i in dictionary.values():
        print (i)
        

kWeakestRows(mat,3)
