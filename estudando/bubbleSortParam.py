#bubbleSort com param left e right

def bubbleSort(array, left, right):

    for i in range(right - left + 1):

        for j in range(left, right - i):
            
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

array = [13, 5, 8, 36, 9, 4, 0]
bubbleSort(array, 1, 5)
print(array)