def follow(instructions: str) -> tuple[int, int] | list[int]:
    # your code here
    listains = list(instructions)
    x = 0
    y = 0
    for letra in listains:
        match letra:
           case "f":
                x += 1
           case "b":
                x -= 1
           case "r":
                y += 1
           case "l":
                y -= 1
    lista = [y,x]
    return lista


print("Example:")
print(list(follow("ffbbffbb")))
