from enum import Enum

class bmi_ertekek(Enum):
    Sovány = 18.5
    Normál = 25
    Túlsúlyos = 30
    Extrém_túlsúlyos = 40

tomb = []

class bmi:
    def __init__(self, kor):
        self.kor = kor
        self.tomeg = self.tomeg()
        self.magassag = self.magassag()

    def show(self):
        print(self.kor)
        self.tomeg.show()
        self.magassag.show()

    class tomeg:
        def __init__(self, tomeg):
            self.tomeg = tomeg

    class magassag:
        def __init__(self, magassag):
            self.magassag = magassag

fki = open("mérések.txt","r+", encoding="utf8")

for sor in fki:
    sor = sor.strip().split()
    tomb.append(sor)

for sor in tomb:
    try:
        print("%s" %sor[0])

        bmi.kor = int(input("- Kor: "))
        sor.append("- Kor:")
        sor.append(str(bmi.kor))
        sor.append("éves |")

        bmi.tomeg = float(input("Tömeg: "))
        sor.append("Tömeg:")
        sor.append(str(bmi.tomeg))
        sor.append("kg |")

        bmi.magassag = float(input("Magasság: "))
        sor.append("Magasság:")
        sor.append(str(bmi.magassag))
        sor.append("cm |")

        kalkul = bmi.tomeg / ((bmi.magassag / 100) ** 2)
        sor.append(" -->  BMI: ")
        sor.append(str(kalkul))

        if kalkul < bmi_ertekek.Sovány.value:
            sor.append("- %s //" %bmi_ertekek.Sovány.name)
        if kalkul >= bmi_ertekek.Sovány.value and kalkul < bmi_ertekek.Normál.value:
            sor.append("- %s testsúly //" %bmi_ertekek.Normál.name)
        if kalkul < bmi_ertekek.Túlsúlyos.value and kalkul >= bmi_ertekek.Normál.value:
            sor.append("- %s //" %bmi_ertekek.Túlsúlyos.name)
        if kalkul >= bmi_ertekek.Túlsúlyos.value and kalkul < bmi_ertekek.Extrém_túlsúlyos.value:
            sor.append("- Elhízás //")
        if kalkul > bmi_ertekek.Extrém_túlsúlyos.value:
            sor.append("- Extrém elhízás //") #de a list index 0 nem jó - ugorja át azt a sort ami üres
    except ZeroDivisionError:
        print("A nulla nem jó érték.")

fki.truncate()
fki.seek(0)

for sor in tomb:
    x=(' '.join(sor))
    fki.write(x+'\n')

fki.close()