numeros = [6, 2, 9, 6, 4, 1, 6]
ja_mostradas = []
for numero in numeros:
    contador = 0
    for n in numeros:
        if numero == n:
            contador +=1

    if contador >1 and numero not in ja_mostradas:
       print(numero)
       ja_mostradas.append(numero)
    