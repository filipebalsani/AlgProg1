a = float(input("Lado A:"))
b = float(input("Lado B:"))
c = float(input("Lado C:"))

maior = 0

if a < b+c and b < a+c and c < a+b:
    if a == b and b == c:
        print("é um triângulo equilátero")
    elif a == b or b == c or c == a:
        print("é um triangulo isóceles")
    else:
        print("é um triangulo escaleno")
else:
    print("nao pode ser triangulo")

