values = []
for number in range(1, 6):
 values.append(number ** 2)

values_comp = [number ** 2 for number in range(1, 6)]
print(values)
print(values_comp)

even=[number for number in range(1, 51) if number%2==0]
print(even)
odd=[number for number in range(1, 51) if number%2!=0]
print(odd)