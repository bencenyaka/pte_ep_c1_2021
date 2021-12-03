'''def megtalal():
    szoveg = input ("Kérek egy szöveget: ")
    karakter = input ("Keresendő karakter a szövegben: ")
    i = 0

    for kar in szoveg:
        i+=1
        if i==karakter:
            return i
        else:
            return -1

megtalal()
'''

#def megtalal(karakter: str, szoveg: str) -> int:
#    '''
#
#    :param karakter: keresendő karakter
#    :param szoveg: szöveg amiben keressük
#    :return: karakter szövegbeli indexe
#    '''
#    i=-1
#    for  i in range(len(szoveg)):
#        if szoveg[i]==karakter and i==-1:
#            return i

#    return -1

#megtalal()


#def megtalal2(karakter: str, szoveg: str) -> int:
#    '''

#    :param karakter: keresendő karakter
#    :param szoveg: szöveg amiben keressük
#    :return: karakter szövegbeli indexe
#    '''
#    pozicio = -1
#    i = 0
#    while pozicio == -1 and i < range(len(szoveg)):
#        if szoveg[i]==karakter and i==-1:
#            pozicio = i
#        i += 1
#    return pozicio

#megtalal2()



'''def kacsanevek(prefixes='JKLMNOPQ', suffix='ack') -> None:
    nevek = []
    for kezdo_betu in prefixes:
        nevek.append(kezdo_betu + suffix)
    return nevek'''

#print(megtalal('a','Indul a pap aludni.'))

#print(megtalal2('a','Indul a pap aludni.'))

#print('Indul a pap aludni.'.find('a'))

#print(kacsanevek())

