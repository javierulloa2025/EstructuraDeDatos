from threading import Timer

arr = [20, 5, 100, 1, 90, 200, 40, 29, 2000]

for item in arr:
    Timer(item / 1000, lambda x=item: print(x)).start()
