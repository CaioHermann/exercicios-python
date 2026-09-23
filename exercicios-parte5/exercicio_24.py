lista = [5, 12, 8, 20, 3, 15]
numeros_maior_que_10 = []
for numero in lista:
    if numero > 10:
        numeros_maior_que_10.append(numero)
print(f"Quantidade de números maiores que 10: {len(numeros_maior_que_10)}\nNúmeros: {numeros_maior_que_10}")