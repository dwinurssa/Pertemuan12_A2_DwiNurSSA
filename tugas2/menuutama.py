from luas.menu import menu
from luas.persegi import l_persegi
from luas.lingkaran import l_lingkaran
from luas.segitiga import l_segitiga

#Mencetak Menu
menu()
while True:
    masukkan = input("Masukkan pilihan Anda : ")
    if masukkan == "1":
        l_persegi()
    elif masukkan == "2":
        l_lingkaran()
    elif masukkan == "3":
        l_segitiga()
    elif masukkan == "4":
        exit()
    else :
        print("Pilihan Anda tidak terdaftar")
