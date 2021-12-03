print(chr(80),chr(121),chr(116),chr(104),chr(111),chr(110), sep='')
print(ord("P"))
print(ord("y"))
print(ord("t"))
print(ord("h"))
print(ord("o"))
print(ord("n"))
print(ord(chr(80)))
print(type(float("3.5")))
print(int("12"))
print(int("12", base=16)) #tizenhatos számrendszer -> átalakítja decimálissá
print(hex(18))
print(oct(18))
print(bin(18))
number = 23.325236
print(number)
print(round(number))
print(round(number, 2))
print(round(number, 0))

chr(99999)
print(float("5"))

a, b = 2, 4
if a == 4 or b != 4:
    print("nyert")
if a == 4 or b == 4:
    print("majdnem nyert")

#2 nyert, 1 vesztett, 4 vesztett, 3 vesztett
number = 4
if number != 2:
    print("vesztett")
elif number == 3:
    print("kis türelmet kérek")
else:
    print("nyert")

a, b = 5, 2
if a == 5 and b < 2:
    print("nyert")
