#Faça um algoritmo para receber um numero qualquer e imprimir na tela se  o numero é par ou impar, positivo ou negativo.

num = int(input("Digite um numero qualquer: "))
mensagem = " "
if num % 2 == 0 and num < 0:
    mensagem = "Par e Negativo"
elif num % 2 == 0 and num >= 0:
    mensagem = "Par e Positivo"
elif num % 2 != 0 and num < 0:
    mensagem = "Impar e Negativo"
else:
    mensagem = "Impar e Positivo"
print(mensagem)