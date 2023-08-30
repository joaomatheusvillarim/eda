#insertionSort em Python

def insertionSort(array):

    n = len(array)

    for i in range(1, n):
        for j in range(1, n):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                j -= 1

                
array = [13, 5, 8, 36, 9, 4, 0]
insertionSort(array)
print(array)