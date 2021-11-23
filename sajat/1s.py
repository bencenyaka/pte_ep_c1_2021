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

bmi.kor = int(input("Kor: "))
bmi.tomeg = float(input("Tömeg: "))
bmi.magassag = float(input("Magasság: "))

kalkul = bmi.tomeg/((bmi.magassag/100)**2)


fki = open ("mérések.txt","a")
fki.write("Kor: %d; " %bmi.kor)
fki.write("Tömeg: %f; " %bmi.tomeg)
fki.write("Magasság: %f --> " %bmi.magassag)
fki.write("BMI: %f - " %kalkul)

if kalkul<18.5:
    fki.write("Sovány \n")
if kalkul>=18.5 and kalkul<=24.9:
    fki.write("Normál testsúly \n")
if kalkul<=29.9 and kalkul>=25:
    fki.write("Túlsúly \n")
if kalkul>=30 and kalkul<=39.9:
    fki.write("Elhízás \n")
if kalkul>40:
    fki.write("Extrém elhízás \n")

fki.close()