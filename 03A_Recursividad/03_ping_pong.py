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


ping(15)
pong(15)