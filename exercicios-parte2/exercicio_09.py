media = float(input("Insira sua média: "))
if media <= 4:
    resultado = "Reprovado"
elif media <=5.9:
    resultado = "Em Recuperação"
elif media >= 6:
    resultado = "Aprovado"
print(f"Você está atualmente: {resultado}")