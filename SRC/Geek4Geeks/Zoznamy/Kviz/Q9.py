a = 'Geeks 22536 for 445 Geeks'
b = [x for x in (int(x) for x in a if x.isdigit()) if x % 2 == 0]
print(b)
