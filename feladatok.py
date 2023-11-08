import random
import math
def veletlen():
    i:int = 0
    while i<10:
        szam:int = math.floor(random.random()*21+10)     
        print(szam)
        i+=1   
        
def lotto():
    i:int = 0
    while i<5:
        szam:int = math.floor(random.random()*90+1)
        print(szam)
        i+=1
def masodik():
    szam:int = math.floor(random.random()*90+10)
    if szam % 2 ==0:
        print(f"{szam} Páros")
    else:
        print(f"{szam} Páratlan")

def harmadik():
    i:int = 0
    b:int =0
    while i < 15:
        szam:int = math.floor(random.random()*2)
        if szam == 1:
            b+=1
        i+=1
    print(b)

def negyedik():
    szam:int = math.floor(random.random()*14+1)
    osszeg = (((((szam*3)-15)/6)*2)-szam)
    print(szam)
    if osszeg == 5:
        print("Egyenlő")
    else:
        print("Nem egyenlő")

def otodik(a):
    hossz= len(a)
    if hossz >= 5:
        print(hossz)
        print(a.upper()[4])
    else:
        print(hossz)