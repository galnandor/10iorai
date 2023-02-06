from re import A
from zipfile import ZipExtFile


print("Hello üdv itt!")
print(23*12)
print("23*12 =", 23*12)
print("2343*3454 =", 2343*3454)
print("1 kg kenyér =", 800)
print(800 ,"= 1 kg kenyér")
#print("23*12 ="+23*12) #hibás
#print("23*12 ="+(23*12) ) hibás
print("Alma"+" "+"körte")
print("Alma","körte")
print("Alma","körte",sep=", ")
print("Alma","körte","barack", sep="\a") # azonos ""-@
print("Alma","körte","barack", sep="\b") # back space
print("Alma","körte","barack", sep="\b\b\b") #
print("Alma","körte","barack", sep="\f") # sor le - form feed
print("Alma","körte","barack", sep="\n") # új sor
print("Alma","körte","barack", sep="\r") # sor elejere 
print("Alma","körte","barack", sep="\t") # tab              
print("Alma","körte","barack", sep="\xab")  
print("Alma","körte","barack", sep="\x41") 
print("Alma","körte","barack", sep="\v") # sor le
print("Alma","körte","barack", sep="\033") #
print("Alma","körte","barack", sep="\x07") #
print("Szia \\ pipacs") 
print("Szia \' pipacs") 
print("Szia \" pipacs\"")
print("Szia ""pipacs")
#print("Szia "pipacs") 
print('Szia', end="")
print('pipacs')

print('Szia' ,end=" ")
print('pipacs')
print("alma")
