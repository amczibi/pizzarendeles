tipus = []
meret = []
feltet = []
ar = []

def adatbekeres(kerdes):
    adat = input(kerdes)
    return adat

def pizza():

    lead = "igen"
    while (lead == "igen"):
        tip = adatbekeres("Milyen típusú pizzát kér? ")
        mer = adatbekeres("Milyen méretű pizzát kér? ")
        fel = adatbekeres("Kér extra feltétet? ")
        lead = adatbekeres("Szeretne még rendelést leadni? Igen/Nem ")

        tipus.append(tip)
        meret.append(mer)
        feltet.append(fel)

    kiiras()


def kiiras():
    i = 0
    while (i < len(tipus)):
        print(f"{tipus[i]}, {meret[i]}, {feltet[i]}")
        i = i + 1
