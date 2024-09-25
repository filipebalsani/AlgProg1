a = int(input("Digite o 1o termo da equação de 2o grau (x^2):"))
b = int(input("Digite o 2o termo (x):"))
c = int(input("Digite o 3o termo (c):"))
delta = float(b*b - 4*a*c)

if delta < 0 or a == 0:
    print("Não existe raiz real")
elif delta == 0:
    raiz = -1*b / 2*a
    print(f"Existe uma raiz x = {raiz}")
else:
    print(delta ** 0.5,-1*b,2*a)
    r1 = ((-1*b) + (delta**0.5)) / (2*a)
    r2 = ((-1*b) - (delta**0.5)) / (2*a)
    print("Existem duas raizes: x1 =",r1,"x2 = ",r2)
