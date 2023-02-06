
''' 
végtelen ciklus
while True:
    print("ismét")
    print("2. sor")
print("ciklus után")


while False:
    print("ismét")
print("ciklus után")

folytat=True
folytat=False
while folytat:
    valasz=input("Folytatod ? (i/n)")
    if valasz == 'i':
         folytat=True
    else:
         folytat=False

ciklusValtozo=0
while ciklusValtozo < 10:
    print(ciklusValtozo, end=" ")
    ciklusValtozo +=1
print()


print("ciklus után")

#print("\nciklus után")

szam=0
while szam != 10:
    szam+= 1
    print(szam," ",szam * szam)

szam= 100
while szam !=48:
    print(szam , end=" ")
    szam-= 2
'''
'''
a1=1
a2=1
a3=1
while a3 < 1000:
    a3=a1+a2
    a1=a2
    a2=a3
    print(a3,end="\n")

x=1/7
while x < 1:
    x = x + 1/7
    print(x)

 # for ciklus helyett

sor = {"alma","szilva","ló",4}
  # print(type(sor))

for i in sor:
    print(i)

sor = {"alma","szilva","ló",4,"ló"}
for i in sor:
    print(i,end=",")
print()

sor = {"alma","szilva","ló",4,"ló"}
for i in sor:
    print(i,end=",")

for i in range(10):
    print(i,end=",")
print()

for i in range(1,10):
    print(i,end=",")
print()

for i in range(1,10,2):
    print(i,end=",")
print()

for i in range(10,1,-1):
    print(i,end=",")
print()

for i in range(1,101):
    print(i,i**2,sep=", ")
    print(str(i)+", "+str(i**2))
    print(i,", ",i**2)
print()

szam=1;
for sor in range(1,11):
    for oszlop in range(1,11):
        print(szam,end="\t")
        szam +=1
    print()


print()
print()
print()
'''

szam=1/25
x=0
i=0;
while (abs (1 - x) > 0.0001):
    x = x +szam 
    i +=1
    print(i,x)
#    if (i == 8 ):
#        break

print("az összeg =",x)

while True:
    break