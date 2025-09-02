productos = (
        ("Huevo", 50, 30),
        ("Leche", 25, 20),
        ("Pan", 10, 40),
        ("Azucar", 30, 20)
)
total = 0
for producto, precio, stock in productos:
    print(f"{producto} en total ${precio*stock}")
    total += precio*stock
print(f"El total es: ${total}")