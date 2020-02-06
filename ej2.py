numero = int(input("dame un numero entero positivo: "))

if(numero % 2 == 0):
    print(str(numero) + " es par")
else:
    print(str(numero) + " no es par")

encontrado = False

for num in range(1,numero + 1):
    if(numero / num != 0):
        encontrado = True
        break

if(encontrado):
    print(str(numero) + " es primo")
else:
    print(str(numero) + " no es primo")
       
    