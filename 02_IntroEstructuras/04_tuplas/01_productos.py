productos = (
   ("leche", 45, 10),
   ("huevo", 40, 20),
   ("pan", 10, 40)
)
total = 0
for producto, precio, stock in productos:
    print(f"Producto: {producto} ${precio*stock} en producto")
    total += precio*stock
print(f"En total: ${total}")