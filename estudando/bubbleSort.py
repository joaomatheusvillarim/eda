#bubbleSort

def bubbleSort(array):

    length = len(array)

    for i in range(0, length):

        for j in range(0 , length - i - 1):
            
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

array = [13, 5, 8, 36, 9, 4, 0]
bubbleSort(array)
print(array)