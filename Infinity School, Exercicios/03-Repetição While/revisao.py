#Tabuada com Condicional: Faça um programa que solicite um número ao usuário e use um laço while para exibir a tabuada desse número (de 1 a 10), mas apenas para os resultados que forem múltiplos de 3.

contador = 1
numero = int(input("Digite um número: "))
multiplicacao = 0
while contador <= 10:
    multiplicacao = numero * contador
    contador +=1
    if multiplicacao % 3 ==0:
        print(f"O valor é {multiplicacao}")



#Crie um programa que solicite ao usuário a entrada de 5 números inteiros. Utilize um contador para controlar quantas vezes o loop foi executado. Utilize um acumulador para somar os números digitados. Ao final, calcule e exiba a média dos números.

#acumulador = 0
#contador = 0
#while contador < 5:
#    numero = int(input(f"Digite {contador + 1} número: "))
#    contador += 1
#    acumulador += numero
#media = acumulador / contador
#print(f"A média dos números é {media}")