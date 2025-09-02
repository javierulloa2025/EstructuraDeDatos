str1 = "apple"
str2 = "bpple"
permitido = 0
diferencias = 0

lstr1 = list(str1)
lstr2 = list(str2)


def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    # your code here
    lstr1 = list(str1)
    lstr2 = list(str2)
    diferencias = 0
    
    # Comparar posiciones comunes
    for elem1, elem2 in zip(lstr1, lstr2):
        if elem1 != elem2:
            diferencias += 1

    # Sumar diferencias por longitud distinta
    diferencias += abs(len(lstr1) - len(lstr2))

    print(f"diferencias {diferencias}, permitido {permitido}" )
    print(diferencias <= threshold)
    return diferencias <= threshold

fuzzy_string_match(str1, str2, permitido)