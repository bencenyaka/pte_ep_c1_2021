tomb=[]

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


fki = open ("mérések.txt","r+")


for sor in fki:
    sor = sor.strip().split()
    tomb.append(sor)


for sor in tomb:
    bmi.kor = int(input("Kor: "))
    sor.append("Kor:")
    sor.append(str(bmi.kor))
    sor.append("év |")
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

fki.seek(0)
fki.truncate()

for sor in tomb:
    x=(' '.join(sor))
    fki.write(x+'\n')


'''fki.write("Kor: %d; " %bmi.kor)
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
'''
fki.close()