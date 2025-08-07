# import math

# String data type

# literal assignment
first = "Dave"
last = "Gray"

# Opakovanie riadkov Shift+Alt+Up Arrow
print(type(first))
print(isinstance(first, str))

# constructor function
# skopírovanie predchádzajúcich riadkov - vyberieme slovo first a pomocou ctrl + d ďalšie slova first
# pizza = str("Peperroni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation - spojenie
# fullname = first + last

# Escaping special characters
# sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\located'
# print(sentence)

# Multiple lines
# multiline = '''
# Hey, how are you?

# I was just checking in.
#                         All good?
# '''

# String Methods - pomocou shift+alt + šipka dole napokírovať riasky
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good", "ok"))
# print(multiline)

# print(len(multiline))
# multiline += "                                    "
# multiline = "                 " + multiline
# print(len(multiline))

# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

# print("")

# Aktuálne - 1:03:10
# Build a menu - # https://youtu.be/H2EJuAcrZYU?t=3870
# title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") +"$1".rjust(4))
# print("Muffin".ljust(16, ".") +"$2".rjust(4))
# print("Cheescake".ljust(16, ".") +"$4".rjust(4))

# print("")

# https://youtu.be/H2EJuAcrZYU?t=3936
# String index values
# prvy znak je s hodnotou 0 -
# print(first[1])
# print(first[-1])
# print(first[1:-1]) # posledny znak z pohladu rozsahu
# print(first[1:])

# Some methods return boolean data
# print(first.startswith("D"))
# print(first.endswith("Z"))
# vzdy chceme vyskúšať metódy objektu (premenná je objaktov v programovaciom jazyku) - ukázať dopĺňanie Visual Studiom Code

# print("")

# Boolean data types
# hodnota pravda True musí byť s veľkým písmenom
# myvalue = True
# x = bool(False)
# print(type(x))
# print(isinstance(myvalue, bool))

# Numeric data types

# integer type
# price = 100
# best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int))

# float type
# gpa = 3.28
# y= float(1.14)
# print(type(gpa))

# complex type - nebudeme riešiť je pre inžinierov a mimo pochopenia

# Built-in functions for numbers
# print(abs(gpa))
# print(round(gpa))
# print(round(gpa, 1))

# import math
# print(math.pi)
# print(math.sqrt(64))
# print(math.ceil(gpa))  # zaokruhlenie hore
# print(math.floor(gpa))  # zaokruhlenie dole

# Casting a string to a number
# zipcode = "10001"
# zip_value = int(zipcode)
# print(type(zip_value))

# https://youtu.be/H2EJuAcrZYU?t=4764

# Error if you attempt to cast incorrect data
# zipcode = int("Modra") # sposobi chybu
