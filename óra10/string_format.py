number = 5
number2 = number * 2
print("A szám:", number, "\b, ha megszorzom kettővel akkor", number2, "\b-t kapok.")
print("A szám:", number, ", ha megszorzom kettővel akkor", number2, "-t kapok.")
print(f"A szám: {number}, ha megszorzom kettővel akkor {number2}-t kapok.")
print("A szám: {}, ha megszorzom kettővel akkor {}-t kapok.".format(number,number2))

#igazítások
print(f"A szám: {number:<2}, ha megszorzom kettővel akkor {number2:<2}-t kapok.")


#számformátum
number = 13
print(f"A szám: {number:o}, ha megszorzom kettővel akkor {number2:o}-t kapok.")
print(f"A szám: {number:b}, ha megszorzom kettővel akkor {number2:b}-t kapok.")
print(f"A szám: {number:x}, ha megszorzom kettővel akkor {number2:x}-t kapok.")
print(f"A szám: {number:X}, ha megszorzom kettővel akkor {number2:X}-t kapok.")
print(f"A szám: {number:d}, ha megszorzom kettővel akkor {number2:d}-t kapok.")

#unicode karakter
number = 65
print(f" {number:c}")

