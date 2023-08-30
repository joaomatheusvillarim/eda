#insertionSort com param left e right

def insertionSort(array, left, right):

    for i in range(left+1, right+1):
        for j in range(left, right+1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                j -= 1 

                
array = [13, 5, 8, 36, 9, 4, 0]
insertionSort(array, 1, 5)
print(array)