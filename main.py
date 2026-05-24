n = int(input("Son kiriting: "))
tub = True

if n < 2:
    tub = False
else:
    for i in range(2, n):
        if n % i == 0:
            tub = False
            break

if tub:
    print("Tub son")
else:
    print("Tub emas")
