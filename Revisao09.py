#usando for, mostre os numeros pares de 1 a 100, mas em ordem decrescente.
for i in range(100,0,-1):
    if i % 2 == 0:
        print(i, end= " ")