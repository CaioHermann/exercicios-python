while True:
    entrada = input("Insira dois números separados por espaço: ").strip().split(" ")
    
    if len(entrada) != 2:
        print("Erro: insira exatamente dois números.")
        continue
    
    if not (entrada[0].isdigit() and entrada[1].isdigit()):
        print("Erro: insira apenas números.")
        continue
    
    break

print(int(entrada[0]) + int(entrada[1]))
# Se você estiver lendo isto, neste exercício eu tentei me testar para ver até onde eu conseguia complicar um simples exercício,
# Os outros vão ser simples (Eu acho)