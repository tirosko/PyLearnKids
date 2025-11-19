valid_numbers = []

for x in range(1000, 10000):
    third = x / 3
    half = x / 2
    double = x * 2
    triple = x * 3

    if all(1000 <= val <= 9999 for val in [third, half, double, triple]):
        valid_numbers.append(x)

print(f"Počet čísel: {len(valid_numbers)}")
print("Príklady:", valid_numbers[:10])  # prvých 10 čísel na ukážku