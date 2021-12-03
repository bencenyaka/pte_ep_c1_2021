my_str = ""
my_list = []
my_tuple = ()
my_dict = {}

my_tuple2 = (42,32,13,564,567,675)
print(my_tuple2, len(my_tuple2), my_tuple2[2])
my_dict['kulcs'] = 'érték'
my_dict['alma'] = 'apple'
my_dict['egér'] = 'mouse'
print(my_dict)
print(my_dict['alma'])


def beolvasas(filepath: str):
    szinek = {}
    fileobject = open(filepath, 'r')
    for row in fileobject:
        row_datas = row.strip().split()
        szinek[row_datas[1]] = (row_datas[3], row_datas[4], row_datas[5])
    fileobject.close()
    return szinek

szin_szotar = beolvasas('color2.csv')
print(type(szin_szotar))
print(type(szin_szotar["Narancs"]))
print(len(szin_szotar))
print(szin_szotar['Narancs'])
print(szin_szotar.get('kutya', 'Nincs ilyen'))
print('kutya' in szin_szotar)
print(szin_szotar.keys())
print(szin_szotar.values())
print(szin_szotar.items())

szin_szotar2 = szin_szotar.copy()
szin_szotar3 = szin_szotar
print(len(szin_szotar), len(szin_szotar2), len(szin_szotar3))
del(szin_szotar2['Narancs'])
print(len(szin_szotar), len(szin_szotar2), len(szin_szotar3))
szin_szotar3.clear()
print(len(szin_szotar), len(szin_szotar2), len(szin_szotar3))