v1 = []
v2 = []
v3 = []

for i in range(3):
    elem = int(input(f"vetor A elem {i+1}: "))
    v1.append(elem)


for i in range(3):
    elem = int(input(f"vetor B elem {i+1}: "))
    v2.append(elem)

for i in range(3):
    elem = v1[i]*v2[i]
    v3.append(elem)

for i in range(3):
    print(f"{v3[i]} ", end='')

print("\nFIM")
