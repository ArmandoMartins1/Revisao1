#faça um agoritmo que calcule o imc (indice de massa corporal) de uma pessoa, leia o seu peso e a sua altura, imprima na tela sua condição de acordo com  a tablea abaixo:
#formula: IMC=peso/altura^2
#
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura**2)
if imc < 18.6:
    mensagem = "Abaixo do peso"
elif (imc >= 18.6) and (imc <25):
    mensagem = "Peso ideal(parabéns)"
elif (imc >= 25) and (imc <30):
    mensagem = "Levemente acima do peso"
elif (imc >=30) and (imc <35):
    mensagem = "Obesidade grau I"
elif (imc>=35) and (imc < 40):
    mensagem = "Obesidade grau II(severa)"
elif imc >= 40:
    mensagem = "Obesidade grau III(morbida)"
print(mensagem)
