#quick sort which sorts in bigger or lower

A = [8,16,1]

#Use last number as pivoit

def quick_sort (sequence):

    lenght = len(sequence)

    if lenght <= 1:
        return sequence
    else:
        pivot = sequence.pop() #This, you will take the last number 

    item_greater = []
    item_lower = []

    for item in sequence:
        if item > pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)
    

    return quick_sort(item_lower) +  [pivot] + quick_sort(item_greater)  

print (quick_sort(A))
