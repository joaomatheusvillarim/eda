#counting sort

#countingSort sem números negativos e sem repetição
def countingSort(array):
    k = 0
    for i in array:
        if i > k:
            k = i
    aux = list(map(eval, ("False " * k).split()))
    for i in range(len(array)):
        aux[array[i] - 1] = True
    
    retorno = []
    for i in range(k):
        if aux[i]:
            retorno.append(i + 1)
    return retorno

array = [4, 2, 8, 3, 6]
print(countingSort(array))