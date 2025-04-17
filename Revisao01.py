#faça um algoritmo que leia os valores de A,B,C e em seguida imprima na tela a soma entre A e B e mostre se a soma é menor que C

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
soma = a+b
if soma < c:
    print(f"a soma {a} + {b} = {soma}, é menor que {c}")
else:
    print(f"A {soma} é maior igual a {c}")