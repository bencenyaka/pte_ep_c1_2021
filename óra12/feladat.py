def menu_opciok():
    print("Válasszon az alábbi menüpontok közül\n\t0 - Kilépés"
          "\n\t1 - új fa rögzítése"
          "\n\t2 - Fajta bekérés")

def egesz_szam_bekerese(koordinata: str):
    szam = ""
    while szam == "":
        try:
            szam = int(input(f"Adja meg a {koordinata} koordinátát: "))
        except ValueError:
            print("Nem egész szám.")

    return szam

def fa_regisztralasa(fak):
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x,y)
    if hely in fak:
        print("itt már van egy fa.")
    else:
        fak[hely] = input("Kérem adja meg a fa  fajtáját: ")
        print("Sikeres regisztráció.")

def szotar_kiiratasa(szotar, filepath):
    fileobject = open(filepath, 'a')
    for kulcs in szotar:
        fileobject.write(str(kulcs[0]))
        fileobject.write("\t")
        fileobject.write(str(kulcs[1]))
        fileobject.write("\t")
        fileobject.write(str(kulcs))
        fileobject.write("\n")
    fileobject.close()

def szotar_betoltes(filepath: str):
    szotar = {}
    file = open(filepath, 'r')
    for sor in file:
        adat = sor.strip().split('\t')
        szotar[int(adat[0]), int(adat[1])] = adat[2]
    file.close()
    return szotar

def fafajta_lekerdezese(fak):
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x,y)
    if hely in fak:
        print(fak[hely])
    else:
        print("Ezen a koordinátán nincs fa.")

menu= ""
fak_szotar_filepath='fak.csv'
fak = {}
while menu!="0":
    menu_opciok()
    menu = input()
    if menu == "1":
        fa_regisztralasa(fak)
    elif menu == "2":
        fafajta_lekerdezese(fak)
szotar_kiiratasa(fak, fak_szotar_filepath)