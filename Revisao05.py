#faça um algoritmo que leia o valor do salario minimo e o valor do salario de um usuario, calcule quantos salarios minimos esse usuario ganha e imprima na tela o resultado. Base do salariominimo: R$1412,00

salarioMinimo= 1412
salarioUsuario = float(input("informe o seu salario: R$ "))
salarioA= salarioUsuario/salarioMinimo
print(f"O Usuário recebe {salarioA:.2f} salario(s) minimo(s).")
