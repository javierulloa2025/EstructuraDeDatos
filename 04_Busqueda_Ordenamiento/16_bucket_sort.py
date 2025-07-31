def bucket_sort(arr, bucket_size=5):
    if len(arr) == 0:
        return arr

    #encontrar valores max y min
    min_val, max_val = min(arr), max(arr)

    #calcular el numero de cubetas necesarias
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(int(bucket_count))]

    #distribuir los elementos en las cubetas
    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[int(index)].append(num)

    #Ordenar cada cubeta (usando insertion sort)
    for bucket in buckets:
        insertion_sort(bucket)

    #concatenar todas las cubetas
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i -1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

#Ejemplo de uso con flotantes
arr_float = [0.42, 0.32, 0.75, 0.12, 0.89, 0.63]
print(f"Arreglo original: {arr_float}")
sorted_float = bucket_sort(arr_float, bucket_size=0.2)
print(f"Arreglo ordenado: {sorted_float}")

# Ejemplo con números negativos
arr_neg = [-0.5, -0.2, 0.7, -0.8, 0.1]
print(f"Arreglo original (negativos): {arr_neg}")
sorted_neg = bucket_sort(arr_neg, bucket_size=0.3)
print(f"Arreglo ordenado (negativos): {sorted_neg}")

# Ejemplo con todos los elementos iguales
arr_equal = [5, 5, 5, 5]
print(f"Arreglo original (iguales): {arr_equal}")
sorted_equal = bucket_sort(arr_equal, bucket_size=1)
print(f"Arreglo ordenado (iguales): {sorted_equal}")

# Ejemplo con enteros
arr_int = [29, 25, 3, 49, 9, 37, 21, 1, 15, 43, 52, 61, 77, 65, 81, 99, 100]
print("Array original (int):", arr_int)
sorted_int = bucket_sort(arr_int, bucket_size=10)
print("Array ordenado (int):", sorted_int)

