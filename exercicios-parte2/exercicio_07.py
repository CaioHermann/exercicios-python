num = []
for i in range (2):
    num.append(int(input("Insira um número: ")))
if num[0] == num[1]:
    print("Os números são iguais!")
else:
    num.sort(reverse=True)
    print(f"O maior é {num[0]}")