#selectionSort

def selectionSort(array):

    n = len(array)

    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if array[menor] > array[j]:
                array[menor], array[j] = array[j], array[menor]

array = [13, 5, 8, 36, 9, 4, 0]
selectionSort(array)
print(array)