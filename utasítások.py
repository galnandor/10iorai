
'''
ismételd=True
while ismételd:
    ismételd=False
    kezdő = int(input("Kérem a kezdő számot: ")) 
    vég = int(input("Kérem a vég számot: "))
    lépés =int(input("Kérem a lépésközt: "))


    if kezdő < vég and lépés > 0:
        while kezdő <= vég:
            print(kezdő)
            kezdő+= lépés

    elif kezdő > vég and lépés < 0:
        while kezdő >= vég:
            print(kezdő)
            kezdő+= lépés
    else:
        print("Hibás adatok")
        ismételd=True
'''

#--------

kezdo=1
veg=12
lepes=-2
for i in range(kezdo,veg,lepes):
    print(i)

kezdo=12
veg=12
lepes=-2
for i in range(kezdo,veg,lepes):
    print(i)

kezdo=12
veg=2
lepes=0
#for i in range(kezdo,veg,lepes):
#    print(i)
