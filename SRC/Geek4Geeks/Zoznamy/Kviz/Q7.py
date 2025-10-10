a = []
a.append([1, [2, 3], 4])
print(a)

a.extend([7, 8, 9])
print(a)
print('--------')
print(a[0])
print(a[0][1])
print(a[0][1][1])
print(a[2])

print(a[0][1][1] + a[2])
