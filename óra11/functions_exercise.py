sebesseg = int(input("Sebesség (km/h): "))
print("m/sec-ben %d" %(sebesseg*3.6))
print("m/sec-ben: ", sebesseg * 3.6)

print("--------------------------------")

import random

rand=[]

paros=[]
ptlan=[]

for i in range(100):
    n = random.randint(0,100)
    rand.append(n)

szam=0
for szam in rand:
    if szam%2 == 0:
        paros.append(szam)
    else:
        ptlan.append(szam)

print(rand,"\n")
print(ptlan,"\n")
print(paros, "\n")

for elem in paros:
    print(elem, end=" ")

print("\n")

for elem in ptlan:
    print(elem, end=" ")

print("\n")

print("-----------------------------------")

import math

a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

if a+b<c or a+c<b or c+b<a:
    print("Nem szerkeszthető.")

d = (a+b+b)/2

k = a+b+c

t = math.sqrt((d*(d-a)*(d-b)*(d-c)))

print("Terület:", t)
print("Kerület:", k)

print("-----------------------------------")

'''
lista = []

while len(lista) == 0 or lista[-1] == '':
    lista.append(input("Szám:"))

lista.remove('')

print(lista)
'''
print("--------------------------------------")

numbers = []

for i in range(20):
    numbers.append(random.randint(1,100))

min = numbers[0]
max = numbers[0]

for number in numbers:
    if min>number:
        min = number
    if max<number:
        max = number

print(numbers)
print(min,max)

print("----------------------------------")

nev = input("Név: ")
nem = input("f-férfi, n-nő: ")

if nem == 'f':
    print("%s úr" %nev)
elif  nem == 'n':
    print("%s asszony" %nev)
else:
    print(nev)

print("------------------------------------")

#def maximum_kereses(lista: list[float]) -> float:
#    '''
#    megkeresi egy valós számot tartalmazó lista maximumát/legnagyobb elemét
#    :param lista: valós számok listája
#    :return: valós számok maximum értéke
#    '''
#    lista = []
#    max = lista[0]
#    for number in lista:
#        if max < number:
#            max = number
#    return max

#print(maximum_kereses(numbers))

def kiiratas(szam: float) -> None:
    print(szam)

kiiratas(2)