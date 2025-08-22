print("**** CALCULADORA ****")

# entrada de dados
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Digite o número da operação: ")

# função para exibir o resultado sem ".0" desnecessário
def formatar(valor):
    if valor.is_integer():   # verifica se é número inteiro
        return int(valor)
    return valor

# processamento
if opcao == "1":
    resultado = numero1 + numero2
    print(f"\nResultado da soma: {formatar(resultado)}")

elif opcao == "2":
    resultado = numero1 - numero2
    print(f"\nResultado da subtração: {formatar(resultado)}")

elif opcao == "3":
    resultado = numero1 * numero2
    print(f"\nResultado da multiplicação: {formatar(resultado)}")

elif opcao == "4":
    if numero2 == 0:
        print("\nNão consigo calcular: divisão por zero!")
    else:
        resultado = numero1 / numero2
        print(f"\nResultado da divisão: {formatar(resultado)}")

else:
    print("\nOpção inválida! Escolha 1, 2, 3 ou 4.")
