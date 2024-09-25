import random

ds = [] # dez sort
ap = []


for i in range(5):
    elem = random.randint(0,49)
    j = 0
    if i > 1:
        while j < i:
            if elem == ds[j]:
                elem = random.randint(0,49)
            j += 1
    ds.append(elem)

  
'''print("before sort:")
for i in range(5):
    print(f"{ds[i], }", end='') '''

for i in range(5):
    for j in range(4):
        if ds[j] > ds[j+1]:
            temp = ds[j]
            ds[j] = ds[j+1]
            ds[j+1] = temp

'''
print("\nafter sort:")
for i in range(5):
    print(f"{ds[i], }", end='') '''
    
for i in range(10):
    elem = int(input(f"Aposta {i+1}: "))
    ap.append(elem)
    

    

c = 0

for i in range(10):
    for j in range(5):
        if ap[i] == ds[j]:
            c+=1
            
for i in range(5):
    print(f"{ds[i]}  ", end='')

print(f"\n{c} acertos.")

print("\nFIM")
