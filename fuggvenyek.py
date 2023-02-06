# függvényekről
def teszt(nev):
    print("Szia "+nev+"!")

teszt("Pisti") 
teszt("Zoli") 
teszt("Karcsi") 
teszt("Ági")
# print(nev)
def negyzet(x):
    n=x*x
#    print(n)
    return n

negyzet(3)
print(negyzet(3))

harom=negyzet(3)
negy=negyzet(4)
ot=negyzet(5)
print((harom+negy)/ot)

for i in range(1,101):
    x=negyzet(i)
    print(i,x)
print(x)



def kiIr(Lista):
    for x in Lista:
        print(x,end=",")
    print()

print("-------------------------------")
l=list()
l=[1,12,2,3]
print(l.index(12))
print("-------------------------------")

def kiIr2(lista):
    for x in range(len( lista)):
        print(i.lista(1))

en_Listam=(1,2,3,4,2,3)
print(type(en_Listam))
print(en_Listam)

kiIr(en_Listam)
kiIr2(en_Listam)

en_Listam=[1,2,3,4,2,3]
print(type(en_Listam))
print(en_Listam)

kiIr(en_Listam)
kiIr2(en_Listam)

en_Listam={1,2,3,4,2,3}
print(type(en_Listam))
print(en_Listam)

kiIr(en_Listam)
#kiIr2(en_Listam)

