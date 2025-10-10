a = [x for x in range(5)]
b = [x for x in range(7) if x in a and x % 2 == 0]
c = [x for x in range(7)]

print(a)

print(c)

# Vnoreným príkazom je tak možno vytvárať rôzne zoznamy bez toho aby sme museli prvky zoznamu "vkladať" do nového zoznamu
print('----------')
for x in c:
    if x in a and x % 2 == 0:
        print(x)

print(b)
