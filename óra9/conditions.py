number = 101
if number > 100:
    print("Nagyobb, mint száz.")
else:
    print("Nem nagyobb, mint száz.")

if number % 2 == 0:
    print("Páros.")
else:
    print("Páratlan.")

number1 = 5
number2 = 25
if number1 % number2:
    print("Egyik szám osztható a másikkal.")
else:
    if number2 % number1 == 0:
        print("A másik szám is osztható az elsővel.")
    else:
        print("Nem.")

radar = "szöves"
if radar[0] == radar[-1]:
    print("Megegyezik az első és az utolsó betű.")
else:
    print("Nem egyezik meg.")

num = 3
if num > 0:
    print("Pozitív.")
else:
    if num == 0:
        print("Nulla.")
    else:
        print("Negatív")

num1 = 7
num2 = 6
num3 = 5
if num1 > num2:
    if num1 > num3:
        print("Az első szám a legnagyobb.")
    elif num3 > num1:
        print("A harmadik szám a legnagyobb.")

elif num2 > num1:
    if num2 > num3:
        print("A második szám a legnagyobb.")
    else:
        print("A harmadik szám a legnagyobb.")

elif num1 == num2:
    if num1 == num3:
        print("Egyenlőek.")
    elif num1 > num3:
        print("Az első két szám a legnagyobb.")
    else:
        print("A harmadik szám a legnagyobb.")

numero = 4
if numero >= 3 and numero < 17:
    print("Beleesik.")
else:
    print("Nem esik bele.")

a = 3
b = 1
c = 5

if (a + b > c and b + c > a and a + c > b):
    print("A háromszög szerkeszthető.")
else:
    print("Nem szerkesztehtő.")

try:
    jegy = 3
    #jegy = int(input("Jegy: "))
    if jegy == 5:
        print("Kíváló.")
    elif jegy == 4:
        print("Jó.")
    elif jegy == 3:
        print("Közepes.")
    elif jegy == 2:
        print("Elégéséges.")
    elif jegy == 1:
        print("Elégtelen.")
    else:
        print("Nem jó érték.")
except ValueError:
    print("Nem számjegy.")

try:
    print(type(float(input("Kérek egy valós számot: "))))
except ValueError:
    print("Hibás bemenet.")

print(type(str(9)))
print(type(str(-37.54)))

try:
    szam = input()
    szam = float(szam)
    print(szam*3)
except ValueError:
    print("Nem szám.")