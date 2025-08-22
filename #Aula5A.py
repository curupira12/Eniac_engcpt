# Escreva um programa que verifica se uma pessoa é maior de idade
print("**** Programa Maior de Idade ****")
idade = int(input("Digite a sua idade: "))

if idade > 18:
    print("Parabens, voce é maior de idade!")

if idade >= 18:
    print("Parabens, voce é maior de idade!")

if idade < 18:
    print("Saia desse programa ele não é para você!")

#outro exemplo
idade_valida = range(18, 121)
if idade in idade_valida:
    print("Parabens, voce é maior de idade!")