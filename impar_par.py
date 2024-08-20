# Solicita ao usuário para inserir o primeiro número (A)
A = int(input("Digite o valor de A: "))

# Solicita ao usuário para inserir o segundo número (B)
B = int(input("Digite o valor de B: "))

# Exibe os valores antes da troca
print(f"Antes da troca: A = {A}, B = {B}")

# Troca os valores de A e B
A, B = B, A

# Exibe os valores após a troca
print(f"Após a troca: A = {A}, B = {B}")
