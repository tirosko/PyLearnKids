""" Výraz list[listelements]*N, kde N je celé číslo, pripojí N kópií prvkov zoznamu v pôvodnom zozname. 
Ak je N záporné celé číslo alebo 0, výstup bude prázdny zoznam, inak ak je N kladné, prvky zoznamu sa pridajú N krát do pôvodného zoznamu. """

li = ['a', 'b', 'c'] * -3
print(li)

li = ['a', 'b', 'c'] * 3
print(li)
