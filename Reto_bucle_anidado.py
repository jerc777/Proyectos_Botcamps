numeros = [5, 8, 10, -3, 2, 1, -7]
cont = 1
for numero in numeros:
    print(numero)
    if numero < 0:
        print(f"El {cont}º numero negativo encontrado es el:", numero)
        cont += cont
