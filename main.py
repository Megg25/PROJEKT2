import random

def tajne_cislo():
    num = []
    pocet_cisel = 4
    i = 0
    if pocet_cisel in range(1, 10):
        while i < pocet_cisel:
            cislo = random.randint(1, 9)
            if cislo not in num:
                num.append(cislo)
                i += 1
    return num

def spravna_pozice(tvoje_cislo, vybrane_cislo):
    list_tvoje_cislo = list(tvoje_cislo)
    bulls = 0
    if list_tvoje_cislo[0] == str(vybrane_cislo[0]):
        bulls += 1
    if list_tvoje_cislo[1] == str(vybrane_cislo[1]):
        bulls += 1
    if list_tvoje_cislo[2] == str(vybrane_cislo[2]):
        bulls += 1
    if list_tvoje_cislo[3] == str(vybrane_cislo[3]):
        bulls += 1
    return bulls

def spravne_cislo(tvoje_cislo, vybrane_cislo):
    cows = 0
    for i in list(tvoje_cislo):
        if i in str(vybrane_cislo):
            cows += 1
    return cows

def vyhodnotit(bulls):
    hodnoceni = 0
    if bulls == 0:
        hodnoceni == 0
    if bulls == 1:
        hodnoceni += 1
    if bulls == 2:
        hodnoceni += 2
    if bulls == 3:
        hodnoceni += 3
    if bulls == 4:
        hodnoceni += 4
    return hodnoceni

def statistika(soucet_pokusu):
    vysledek = []
    if soucet_pokusu >= 4:
        vysledek.append("not so good")
    elif soucet_pokusu >= 2:
        vysledek.append("average")
    elif soucet_pokusu >= 0:
        vysledek.append("amazing")
    return vysledek

def hlavni():
    print("Hello, I've generated a random 4 digit number for you.\nLet s play a BULLS and COWS game.")
    vybrane_cislo = tajne_cislo()
    print(vybrane_cislo)
    hodnoceni = 0
    soucet_pokusu = 0
    while hodnoceni != 4:
        tvoje_cislo = input("Enter your 4 digit number: ")
        bulls = spravna_pozice(tvoje_cislo, vybrane_cislo)
        cows = spravne_cislo(tvoje_cislo, vybrane_cislo)
        print(f"{bulls} bulls, {cows} cows")
        hodnoceni = vyhodnotit(bulls)
        soucet_pokusu += 1
        vysledek = statistika(soucet_pokusu)
        if hodnoceni == 4:
            print(f"Congratulation! You´ve guessed the right number in {soucet_pokusu} guesses.")
            print(f"That´s{vysledek}")
            exit()
hlavni()
