import random as r
from time import *

def szamlalo(hossz: int, leptek: int) -> None:
    for i in range(hossz // leptek):
        print(r.randint(0, 1000))
        sleep(leptek)


def primtenyezos_felbontas_kiirasa(szam: int) -> None:
    oszto = 2
    maradek = szam
    while maradek>1:
        if maradek % oszto == 0:
            print(oszto)
            maradek = maradek / oszto
        else:
            oszto = oszto+1