class Kutya:
    '''Kutyák osztálya.'''

    def __init__(self, nev: str, fajta: str):
        self.nev = nev
        self.fajta = fajta

    def __str__(self):
        return "A {} nevű kutya {} fajtájú".format(self.nev,self.fajta)

kutya = Kutya("Bodri", "Kuvasz")
kutya2 = Kutya("Buksi", "Puli")
print(kutya)
print(kutya2)