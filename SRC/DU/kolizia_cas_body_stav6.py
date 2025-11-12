# vytvorený medzikrok pre ponorku a bubliny
# Autor: Jakub Duban 7.A namiesto 6.B

from tkinter import Tk, Canvas
from random import randint
from time import sleep, time

# Načíta funkciu „sqrt“ z knižnice Math.
from math import sqrt

VYSKA = 500
SIRKA = 800

bub_id = list()
bub_r = list()
bub_rychl = list()
bub_out = list()  # zoznam pre bubliny vymazané z rôznych príčin napríklad ak sú mimo obrazovky alebo ak sú na vrchnej hrane

HRANICA_OKRAJA =5  # hranica okrajov obrazovky pre ponorku

MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_RYCH = 10
MEDZERA = 100

BUB_SANCA = 10
LIMIT_CAS = 20
BONUS_SKORE = 1000

skore = 0
bonus = 0
koniec = time() + LIMIT_CAS

okno = Tk()

# Pomenovanie hry
okno.title("Bublinový strelec")
# Nastaví sa tmavo modrá ako farba pozadia (more)
# Vytvorí grafické plátno, na ktoré sa bude kresliť
c = Canvas(okno, width=SIRKA, height=VYSKA, bg="darkblue")
c.pack()

LOD_R = 15

# Nakreslí červený trojuholník ako loď
lod_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill="black")
# Nakreslí červenú kružnicu v strede obrazovky
# Polomer kruhu (veľkosť ponorky)
lod_id2 = c.create_oval(0, 0, 30, 30, outline="red")

# Premenné „STRED_X“ a „STRED_Y“ obsahujú súradnice stredu obrazovky
STRED_X = SIRKA / 2
STRED_Y = VYSKA / 2
c.move(lod_id, STRED_X, STRED_Y)
c.move(lod_id2, STRED_X, STRED_Y)

# Ponorka pôjde pri stlačení klávesov takto rýchlo
LOD_RYCH = 10


# def hyb_lod(udalost):
#     if udalost.keysym == "Up":
#         # Ak sa stlačí šípka nahor, obe časti ponorky stúpajú
#         c.move(lod_id, 0, -LOD_RYCH)
#         c.move(lod_id2, 0, -LOD_RYCH)
#     elif udalost.keysym == "Down":
#         # Tieto riadky sa aktivujú, ak sa stlačí šípka nadol - ponorka klesá.
#         c.move(lod_id, 0, LOD_RYCH)
#         c.move(lod_id2, 0, LOD_RYCH)
#     elif udalost.keysym == "Left":
#         # Ponorka sa po stlačení šípky vľavo hýbe vľavo
#         c.move(lod_id, -LOD_RYCH, 0)
#         c.move(lod_id2, -LOD_RYCH, 0)
#     elif udalost. keysym == "Right":
#         # Po stlačení šípky vpravo sa ponorka hýbe vpravo
#         c.move(lod_id, LOD_RYCH, 0)
#         c.move(lod_id2, LOD_RYCH, 0)

def hyb_lod(udalost):
    if udalost.keysym == "Up":
        x, y = zisti_sur(lod_id2)
        if y > HRANICA_OKRAJA:
            c.move(lod_id, 0, -LOD_RYCH)
            c.move(lod_id2, 0, -LOD_RYCH)
            # print("H", y)
        # print(zisti_sur(lod_id2))
    elif udalost.keysym == "Down":
        x, y = zisti_sur(lod_id2)
        if y < VYSKA - HRANICA_OKRAJA:
            c.move(lod_id, 0, LOD_RYCH)
            c.move(lod_id2, 0, LOD_RYCH)
            # print(y)
        # print(zisti_sur(lod_id2))
    elif udalost.keysym == "Left":
        x, y = zisti_sur(lod_id2)
        if x > HRANICA_OKRAJA:
            c.move(lod_id, -LOD_RYCH, 0)
            c.move(lod_id2, -LOD_RYCH, 0)
            # print(x)
        # print(zisti_sur(lod_id2))
    elif udalost.keysym == "Right":
        x, y = zisti_sur(lod_id2)
        if x < SIRKA - HRANICA_OKRAJA:
            c.move(lod_id, LOD_RYCH, 0)
            c.move(lod_id2, LOD_RYCH, 0)

        # print(zisti_sur(lod_id2))
c.bind_all("<Key>", hyb_lod)


# Prikáže Pythonu, aby spustil „hyb_lod“, keď sa stlačí akýkoľvek kláves
c.bind_all("<Key>", hyb_lod)


def vytvor_bublinu():
    # Nastaví sa pozícia bubliny na plátne
    x = SIRKA + MEDZERA
    y = randint(0, VYSKA)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    if (y + 2*r) <= VYSKA:
        # Tento riadok kódu vytvorí samotnú bublinu
        id1 = c.create_oval(x - r, y - r, x + r, y + r, outline="white")
        bub_id.append(id1)
        bub_r.append(r)
        bub_rychl.append(randint(1, MAX_BUB_RYCH))


def hyb_bubliny():
    # Prejde cez každú bublinu v zozname
    for i in range(len(bub_id)):
        # Posunie bublinu po obrazovke danou rýchlosťou
        c.move(bub_id[i], -bub_rychl[i], 0)

# Táto funkcia zmaže bublinu s ID „i“.


def zmaz_bub(i):
    # Zmaže bublinu zo zoznamu polomerov a rýchlostí
    del bub_r[i]
    del bub_rychl[i]
    # Zmaže bublinu z plátna
    c.delete(bub_id[i])
    # Zmaže bublinu zo zoznamu ID
    del bub_id[i]


def uprac_bubliny():
    # Tu prejdeme zoznam bublín odzadu, aby sme sa vyhli chybe vo „for“ slučke pri zmazaní bubliny
    # zoznamu. Funkcia „zisti_sur“ získa súradnice stredu bubliny s ID „i“. Ak je bublina mimo
    # obrazovky, zavoláme funkciu „zmaz_bub“ s ID bubliny „i“. Funkcia „zmaz_bub“ zmaže bublinu
    # z plátna a zo zoznamov bublín. Funkcia „uprac_bubliny“ zavolá funkciu „bub“ pre každú bublinu.
    for i in range(len(bub_id) - 1, -1, -1):
        # Získa súradnice stredu bubliny s ID „i“. Zisťuje, kde sa bublina nachádza.
        x, y = zisti_sur(bub_id[i])
        # Ak je bublina mimo obrazovky, zmažeme ju - inak by len spomaľovala hru
        if x < -MEDZERA:
            zmaz_bub(i)


def zisti_sur(id):
    poz = c.coords(id)
    # Zistí súradnicu x stredu bubliny
    x = (poz[0] + poz[2]) / 2
    # Zistí súradnicu y stredu bubliny
    y = (poz[1] + poz[3]) / 2
    return x, y


def vzdialenost(id1, id2):
    # Zistí polohu prvého objektu.
    x1, y1 = zisti_sur(id1)
    # Zistí polohu druhého objektu.
    x2, y2 = zisti_sur(id2)
    # Vypočíta vzdialenosť medzi nimi
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def kolizia():
    # Táto premenná si pamätá získané body.
    body = 0
    # Táto slučka prechádza zoznam bublín (ide odzadu, aby sa vyhla chybám pri zmazaní bublín).
    for bub in range(len(bub_id) - 1, -1, -1):
        # Zisťuje kolíziu ponorky s akoukoľvek bublinou.
        if vzdialenost(lod_id2, bub_id[bub]) < (LOD_R + bub_r[bub]):
            # Spočíta body za bublinu a pripočíta ich k celkovému skóre.
            body += (bub_r[bub] + bub_rychl[bub])
            # Zmaže bublinu.
            zmaz_bub(bub)
    # Vráti počet získaných bodov
    return body


def kolizia_HH():  # kolízia s hornou hranicou
    for bub in range(len(bub_id) - 1, -1, -1):
        # Zisťuje kolíziu
        x, y = zisti_sur(bub_id[bub])
        r = bub_r[bub]
        if y - r < 0:
            # if x < SIRKA - 50:
            zmaz_bub(bub)
            # else:
            #     c.itemconfig(bub_id[bub], fill="red")


# Vytvorí nápisy „ČAS“ a „SKÓRE“ na vysvetlenie, čo ktoré číslo znamená.
c.create_text(50, 30, text="ČAS", fill="white")
c.create_text(150, 30, text="SKORE", fill="white")
# Nastaví skóre a zostávajúci čas.
text_cas = c.create_text(50, 50, fill="white")
text_skore = c.create_text(150, 50, fill="white")


def ukaz_skore(skore):
    # Zobrazí skóre.
    c.itemconfig(text_skore, text=str(skore))


def ukaz_cas(zostal_cas):
    # Zobrazí zostávajúci čas.
    c.itemconfig(text_cas, text=str(zostal_cas))


# #HLAVNÁ SLUČKA
while time() < koniec:
    # Vygeneruje náhodné číslo od 1 do 10
    if randint(1, BUB_SANCA) == 1:
        # Ak je náhodné číslo 1, program vytvorí novú bublinu
        # (priemerne 1 z 10-krát - aby bublín nebolo priveľa)
        vytvor_bublinu()
    # Spúšťa funkciu „hyb_bubliny“
    hyb_bubliny()
    uprac_bubliny()
    skore += kolizia()
    kolizia_HH()
    if (int(skore / BONUS_SKORE)) > bonus:
        bonus += 1
        koniec += LIMIT_CAS
    ukaz_skore(skore)
    ukaz_cas(int(koniec - time()))
    # print(skore)
    # Aktualizuje obsah okna, aby sa prekreslili bubliny, čo sa pohli
    okno.update()
    # Spomaľujeru, aby nebolapríliš rýchla
    sleep(0.01)

c.create_text(STRED_X, STRED_Y,
              text="KONIEC_HRY", fill="red", font=("Helvetica", 30))
c.create_text(STRED_X, STRED_Y + 30,
              text="Skóre: " + str(skore), fill="white")
c.create_text(STRED_X, STRED_Y + 45,
              text="Bonusový čas: " + str(bonus + LIMIT_CAS), fill="white")

okno.mainloop()
