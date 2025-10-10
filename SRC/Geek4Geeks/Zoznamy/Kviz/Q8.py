a = [x for x in (x for x in 'Geeks 22966 for Geeks' if x.isdigit()) if
     (x in ([x for x in range(20)]))]
print(a)
