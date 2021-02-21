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

def tvoje_cislo_spravne(tvoje_cislo):
    list_tvoje_cislo = list(tvoje_cislo)
    kontrola_spravnosti = True
    if list_tvoje_cislo[0] == str(0):
        kontrola_spravnosti = False
        print("Sorry, the number entered must not begin with ´0´.")
    if len(list_tvoje_cislo) >= 5 or len(list_tvoje_cislo) <= 3:
        print("Sorry, the number you entered does not have the required length")
        kontrola_spravnosti = False
        exit()
    for n in list_tvoje_cislo:
        if n.isalpha():
            print("Sorry, the number entered cannot contain letters")
            kontrola_spravnosti = False
    return kontrola_spravnosti

def spravna_pozice(tvoje_cislo, vybrane_cislo):
    list_tvoje_cislo = list(tvoje_cislo)
    bulls = 0
    cows = 0
    if list_tvoje_cislo[0] == str(vybrane_cislo[0]):
        bulls += 1
    elif list_tvoje_cislo[0] in str(vybrane_cislo):
        cows += 1
    if list_tvoje_cislo[1] == str(vybrane_cislo[1]):
        bulls += 1
    elif list_tvoje_cislo[1] in str(vybrane_cislo):
        cows += 1
    if list_tvoje_cislo[2] == str(vybrane_cislo[2]):
        bulls += 1
    elif list_tvoje_cislo[2] in str(vybrane_cislo):
        cows += 1
    if list_tvoje_cislo[3] == str(vybrane_cislo[3]):
        bulls += 1
    elif list_tvoje_cislo[3] in str(vybrane_cislo):
        cows += 1
    return bulls, cows

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
    print(vybrane_cislo)  # iba na overenie- ci pocitame spravne!!! potom odstranit!!!
    hodnoceni = 0
    soucet_pokusu = 0
    while hodnoceni != 4:
        tvoje_cislo = input("Enter your 4 digit number: ")
        kontrola_spravnosti = tvoje_cislo_spravne(tvoje_cislo)
        if kontrola_spravnosti == False:
            continue
        bulls, cows = spravna_pozice(tvoje_cislo, vybrane_cislo)
        print(f"{bulls} bulls, {cows} cows")
        hodnoceni = vyhodnotit(bulls)
        soucet_pokusu += 1
        vysledek = statistika(soucet_pokusu)
        if hodnoceni == 4:
            print(f"Congratulation! You´ve guessed the right number in {soucet_pokusu} guesses.")
            print(f"That´s{vysledek}")
            exit()

print(hlavni())
