num = 0
while True:
    num_atual =int(input("Insira um número, digite 0 quando quiser exibir a soma total: "))
    num += num_atual
    if num_atual == 0:
        break
print(f"Número total: {num}")