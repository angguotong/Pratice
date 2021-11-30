S = "BAONXXOLL"

def solution(S):

    compare = ["B", "A" , "L" ,"O", "N"]

    Counted_Dct = {

    }

    for i in compare: 

        if i == "L" or i == "O":
            counter = int(S.count(i) /2)
            Counted_Dct[i] = counter 
        else:
            counter = S.count(i)
            Counted_Dct[i] = counter    

    # print (Counted_Dct.values())

    answer = min(Counted_Dct.values())
    print (answer)

    

solution(S)