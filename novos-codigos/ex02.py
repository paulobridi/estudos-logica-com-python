# Algoritmo que calcula a média e os gastos totais com 12 salários

# Inicializando a lista de salários
salarios = []

# Solicitando ao usuário que digite 12 salários
for i in range(12):
    salario = float(input(f"Digite o salário {i+1}: "))
    salarios.append(salario)

# Variável para armazenar a soma dos salários
soma_salarios = sum(salarios)

# Variável para armazenar o número de salários
numero_de_salarios = len(salarios)

# Calculando a média dos salários
media_salarios = soma_salarios / numero_de_salarios

# Imprimindo a média dos salários
print(f"A média dos salários é: {media_salarios:.2f}")

# Imprimindo os gastos totais com os salários
print(f"Os gastos totais com os salários são: {soma_salarios:.2f}")