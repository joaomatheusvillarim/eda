#bubbleSort using recursion

def bubbleSort(array, left, right):
    if right-left == 1:
        return

    for i in range(left, right-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    bubbleSort(array, left, right-1)

array = [13, 5, 8, 36, 9, 4, 0]
bubbleSort(array, 1, 6)
print(array)