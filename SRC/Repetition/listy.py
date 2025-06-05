zoznam=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(zoznam)
print(type(zoznam))
zoznam.insert(0, "x")
print(zoznam)

def vypis(zoznam):
    for i in zoznam:
        print(i)

def pridaj(zoznam, prvok):
    zoznam.append(prvok)
    return zoznam

def odober(zoznam, prvok):
    if prvok in zoznam:
        zoznam.remove(prvok)
    else:
        print(f"Prvok {prvok} nie je v zozname.")
    return zoznam

def vymaz(zoznam):
    zoznam.clear()
    return zoznam

def zmen(zoznam, index, novy_prvok):
    if 0 <= index < len(zoznam):
        zoznam[index] = novy_prvok
    else:
        print(f"Index {index} je mimo rozsahu zoznamu.")
    return zoznam

def najdi(zoznam, prvok):
    if prvok in zoznam:
        return zoznam.index(prvok)
    else:
        print(f"Prvok {prvok} nie je v zozname.")
        return -1

def obsahuje(zoznam, prvok):
    return prvok in zoznam

def dlzka(zoznam):
    return len(zoznam)

