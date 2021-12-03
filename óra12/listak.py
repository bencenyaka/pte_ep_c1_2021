def rendezes(lista: list[int]) -> list[int]:
    rendezett_lista = lista.copy()
    for i in range(1, len(lista)):
        for j in range(len(lista)-i):
            if rendezett_lista < rendezett_lista[j + 1]:
                seged = rendezett_lista[j]
                rendezett_lista[j] = rendezett_lista[j+1]
                rendezett_lista[j+1] = seged

    return rendezett_lista

lista = [6, 2, 5, 9, 12, 34 ,1 ,4, 72]

print(lista)
print(rendezes(lista))

#----------------------------------------------------------

def minimum(lista: list[int], hanyadik=0) -> int:
    return rendezes(lista)[hanyadik]

def osszeg(lista: list[int]) -> int:
    osszeg = 0
    for elem in lista:
        osszeg += elem

    return osszeg

def atlag(lista: list[int]) -> float:
    return osszeg(lista) / len(lista)