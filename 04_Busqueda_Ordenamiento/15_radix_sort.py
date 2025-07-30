def radixSort(arr):
    max1 = max(arr)  #encontramos el elemento más grande

    exp = 1
    while max1 // exp > 0:
        countingSort(arr, exp) #por cada digito ejecuta counting
        exp *= 10

def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = arr[i] // exp1  % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count [i - 1]

    i = n - 1

    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i=0
    for i in range(0, len(arr)):
        arr[i] = output[i]

#Ejemplo de uso
datos = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(datos)
print(datos)