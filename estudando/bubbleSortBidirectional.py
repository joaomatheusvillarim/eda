#bidirectional bubbleSort

def bubbleSort(array, left, right):
    swapped = True
    while swapped:
        swapped = False
        for i in range(left, right):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
        for j in range(right, left, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                swapped = True
        left +=1
        right -= 1

array = [13, 5, 8, 36, 9, 4, 0]
bubbleSort(array, 0, 6)
print(array)

        