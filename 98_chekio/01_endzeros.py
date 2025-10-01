def end_zeros(a: int) -> int:
    # your code here
    a = str(a)
    ainve = list(a[::-1])
    contador = 0
    for numero in ainve:
        if numero == "0":
            contador += 1
        else:
            return contador
    return contador

print("Example:")
print(end_zeros(10))
