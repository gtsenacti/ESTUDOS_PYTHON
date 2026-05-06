nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(nome, "é maior de idade")
else:
    print(nome, "é menor de idade")

# Lista de notas
notas = [7, 8, 6]

soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)

print("Média:", media)