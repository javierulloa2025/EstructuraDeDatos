import time

def ping(n):
    if n == 0:
        return
    print("ping", n)
    pong(n-1)

def pong(n):
    if n == 0:
        return
    print("pong", n)
    ping(n-1)

# Medición del tiempo
inicio = time.perf_counter()
ping(900)  
fin = time.perf_counter()
print(f"\nTiempo de ejecución total: {fin - inicio:.6f} segundos")