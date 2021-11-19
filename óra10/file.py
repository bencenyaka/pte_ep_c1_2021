try:
    fileobject=open("loren.txt","r")

    tartalom = fileobject.readline()

    print(tartalom)
    print(type(tartalom))
    print(len(tartalom))
    print(fileobject.tell()) #kurzor(?)

    fileobject.close()

except FileNotFoundError:
    print("Nincs ilyen fájl.")


fileobject2 = open("loren5.txt","w")
fileobject2.write("Python")
fileobject2.flush()
fileobject2.write("Python")
fileobject2.close()