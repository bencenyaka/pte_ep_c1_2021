def köszönés(nev: str) :
    print("Hello %s" %nev)

def névbekérés() -> str:
    nev = input("Név: ")
    return nev

köszönés(névbekérés())

def beker() -> str:
    return input("Név: ")

def koszon(nev='') -> None:
    print(f'Szia {nev}')

koszon()
koszon(beker())
#-------------------------------

from datetime import datetime

def aktuálisidő():
    print(datetime.now())

aktuálisidő()

#--------------------------------
import time

def varakozas(masodperc: int):
    aktuálisidő()
    time.sleep(masodperc)
    aktuálisidő()

aktuálisidő()
varakozas(0)

#---------------------------------

def netto() -> int:
    return int(input("Nettó ár: "))

def br_afa() -> int:
    afa = 0.27
    br = (1+afa) * netto()
    print("Az áfa %d százalék így a bruttó ár %d Ft." %(afa*100, br))

br_afa()

def get_afa(termek_ara: int, afa=27)-> float:
    '''

    :param termek_ara: termék ára
    :param afa: %-ban
    :return:
    '''

    return termek_ara * (afa / 100)

def brutto_kiszamitasa(termek_ara: int, afa = 27) -> float:
    return termek_ara + get_afa(termek_ara, afa)

ar = 10000
print(get_afa(ar))
print(brutto_kiszamitasa(ar))