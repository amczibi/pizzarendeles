nev = "Pisti"

def osszeadas():
    global nev
    nev = "Szia " + nev
    print(nev)
    szam1 = adatbekeres("Kérek egy számot: ")
    szam2 = adatbekeres("Kérek egy másik számot: ")
    eredmeny = szam1 + szam2
    kiiras(szam1, szam2, eredmeny, "+")



def kivonas():
    szam1 = adatbekeres("Kérek egy számot: ")
    szam2 = adatbekeres("Kérek egy másik számot: ")
    eredmeny = szam1 - szam2
    kiiras(szam1, szam2, eredmeny, "-")


def adatbekeres(uzenet):
    print("-" * 10)
    szam = float(input(uzenet))
    return szam


def kiiras(szam1, szam2, eredmeny, muv):
    print("-" * 10)
    print("A számolás eredménye")
    print(f"{szam1} {muv} {szam2} = {eredmeny:.2f}")