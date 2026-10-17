#Verificar Status de Taxa de Desconto: Crie um programa que peça ao usuário o preço original de um produto e a quantidade comprada. Use if para verificar se a quantidade é maior que 10 para aplicar um desconto de 10% sobre o total.

#preco = float(input("Digite o preço do produto: "))
#quantidade = int(input("Digite a quantidade comprada: "))

#if quantidade > 10:
#    desconto = preco * 0.9
#    print(f"Você comprou {quantidade} quantidade de produtos, sendo assim você tem direito a 10% de desconto sobre o total da compra, sendo R${desconto:.2f} de desconto!")
#else:
#    print("Você não tem direito a desconto")





#Sistema de Login Simples: Desenvolva um programa que peça ao usuário um nome de usuário e uma senha e use if para verificar se são iguais a "admin" e "1234", respectivamente.

login = input("Digite seu nome de usuário: ")
senha = int(input("Digite sua senha númerica: "))

if login == 'admin' and senha == 1234:
    print("Acesso liberado!")
else:
    print("Acesso Negado")