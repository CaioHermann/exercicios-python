contador_positivos = []
while True:
    num_atual = int(input("Insira um número, digite 0 quando quiser exibir os positivos: "))
    if num_atual > 0:
        contador_positivos.append(num_atual)
    if num_atual == 0:
        break
print(f"Total de números positivos: {len(contador_positivos)}\n Números: \n {contador_positivos}")
