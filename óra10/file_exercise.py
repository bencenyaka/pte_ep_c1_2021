fileobject = open("loren.txt","r")
sor = fileobject.readline()
while len(sor)!=0:
    print(sor)
    sor = fileobject.readline()

fileobject.close()

#*----------------------------------------

fileobject2 = open("loren.txt","r")
max = fileobject2.readline()
for sor in fileobject2:
    if len(max)<len(sor):
        max = sor

print(max)

fileobject2.close()

#-----------------------------------------

fileobject3 = open("loren.txt","r")
fileobject4 = open("loren2.txt","w")
fileobject4.write(fileobject3.read())

fileobject3.close()
fileobject4.close()

#------------------------------------------
fileobject5 = open("loren.txt","r")
fileobject6 = open("loren_copy.txt","w")
szoveg = fileobject5.read()
for karakter in szoveg:
    if karakter==' ':
        fileobject6.write('   ')
    else:
        fileobject6.write(karakter)

fileobject6.close()
fileobject5.close()
#------------------------------------------
fileobject7 = open("loren.txt","r")
fileobject8 = open("loren_copy.txt","r")
fileobject9 = open("loren_harom.txt","w")

sor = fileobject7.readline()
sor2 = fileobject8.readline()
while len(sor)!=0 or len(sor2)!=0:
    fileobject9.write(sor)
    fileobject9.write(sor2)
    sor = fileobject7.readline()
    sor2 = fileobject8.readline()

fileobject7.close()
fileobject8.close()
fileobject9.close()