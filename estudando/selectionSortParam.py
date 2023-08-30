#selectionSort com param left e right

def selectionSort(array, left, right):

    for i in range(left, right + 1):
        menor = i
        for j in range(i + 1, right + 1):
            if array[menor] > array[j]:
                menor = j
        array[menor], array[i] = array[i], array[menor]

array = [13, 5, 8, 36, 9, 4, 0]
selectionSort(array, 1, 5)
print(array)