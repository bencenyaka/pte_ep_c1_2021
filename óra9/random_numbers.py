import random

print(random.randint(2,400))
print(random.random())

r = random.randint(-100,100)
print(r)
if r > 0:
    print("Pozitív.")
else:
    if r == 0:
        print("Nulla.")
    else:
        print("Negatív")