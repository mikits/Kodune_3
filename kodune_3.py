import time
from tkinter import *
from random import *
def A():
	pikkused = set()
	while len(pikkused) < 3:
		maatriks = [[randrange(0,100), randrange(0,100), randrange(0,100)] for i in range(3)]
		for i in range(3):
			summa = sum(maatriks[i])
			pikkused.add(summa)
		pikkused = sorted(pikkused)
		print(pikkused)
	aken = Tk()
	aken.title("Ruudud")
	tahvel = Canvas(aken, width = 600, height = 600, background = "white")
	tahvel.grid()
	varvid = ['blue', 'green', 'red']
	for a in range(3):
		tahvel.create_rectangle(300-pikkused[a]/2,300-pikkused[a]/2, pikkused[a],pikkused[a], outline = varvid[a])
	tahvel.mainloop()
    log('A')
def B():
    sona = input("Sisesta sõna(d): ")[::-1]
    print("Sisestatud sõna tähed vastupidises järjekorras on: ",sona)
    log('B')
def C():
    print("Lubatud käsud: ")
    print("A – Ruutude joonistamine")
    print("B – Vastupidises järjestuses kuvamine")
    print("C – Lubatud käskude kuvamine")
    print("L – Logi kuvamine")
    print("P – Programmi sulgemine")
    log('C')
def L():
    kasutajanimi = input("Sisesta kasutajanimi: ")
    parool = input("Sisesta parool: ")
    file = open("andmed.txt", "r")
    oige_kasutaja = file.readline()
    oige_parool = file.readline()
    file.close()
    if oige_kasutaja = kasutajanimi:
        if oige_parool = parool:
            file.open("logi.txt", "ra")
            print(file.read())
            file.write("Kuvati logi")
def log(kask):
    file = open("logi.txt", "w")
    aeg = time.strftime("%H:%M:%S %d.%m.%Y ")
    file.write(aeg)
    file.write("Sisestati käsk ")
    file.write(kask)
    file.write(": ")
    file.close()
start = input("Sisesta soovitud käsk: ").lower()
if start == 'a':
 	A()
elif start == 'b':
 	B()
elif start == 'c':
	C()
elif start == 'l':
	L()
