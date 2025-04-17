#Faça um algoritmo para receber um numero qualquer e imprimir na tela se  o numero é par ou impar, positivo ou negativo.

#alterar o arquivo, pondo repetição
num = 1
mensagem = "S"
while mensagem == "S" or mensagem == "s":
    num = int(input("Digite um numero qualquer: "))
    if num % 2 == 0 and num < 0:
        print("Par e Negativo")
    elif num % 2 == 0 and num > 0:
        print("Par e Positivo")
    elif num % 2 != 0 and num < 0:
        print("Impar e Negativo")
    elif num % 2 != 0 and num > 0:
        print("Impar e Positivo")
    print("----------------------")
    mensagem = input("Tem outro numero para verificar?\n"
                     "S - CONTINUAR\n"
                     "N - SAIR\n"
                     ": ")

