#recursive selectionSort

def selectionSort(array, left, right):

    if right - left == 1:
        return

    menor = left
    for i in range(left+1, right+1):
        if array[menor] > array[i]:
            menor = i
    array[menor], array[left] = array[left], array[menor]
    selectionSort(array, left+1, right)

array = [13, 5, 8, 36, 9, 4, 0]
selectionSort(array, 0, 6)
print(array)