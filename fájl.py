f = open("1.csv")

print(type(f))

print(f.read())
f.seek(0)
print(f.read())

f.seek(2)
print(f.read())

f.seek(0)
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

print("--------------")
f.seek(0)
for sor in f:
    print(sor)
print("--------------")

f.seek(0)
for sor in f:
    print(sor.replace('\n',''))
print("--------------")

f.seek(0)
teszt=f.read()
print(type(teszt))
print(teszt)

f.seek(0)
teszt=f.readlines()
print(type(teszt))
print(teszt)

print("--------------")

adatsorok = []
f.seek(0)
for sor in f:
    adatsorok.append(sor.replace('\n',''))
print("--------------")
print(adatsorok)

adatsorok = []
f.seek(0)
for sor in f:
    adatsorok.append(sor.replace('\n','').split(','))       #üres sorokat cseréli
print("--------------")
print(adatsorok)

print(adatsorok[0])             #1 lista 1. eleme ([0]= 1.elem)
print(adatsorok[0][0])
print("--------------")

for soe in adatsorok:           #egyesével egymás alá
    for elem in sor:
        print(elem,end=" ")


f.close()