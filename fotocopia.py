# Solicita ao usuário para inserir a quantidade de fotocópias realizadas
quantidade = int(input("Digite a quantidade de fotocópias realizadas: "))

# Inicializa o valor total da fatura
fatura = 0.0

# Calcula o custo das primeiras 10 fotocópias
if quantidade > 0:
    if quantidade <= 10:
        fatura = quantidade * 0.25
    else:
        fatura = 10 * 0.25
        quantidade -= 10

        # Calcula o custo das próximas 20 fotocópias
        if quantidade <= 20:
            fatura += quantidade * 0.20
        else:
            fatura += 20 * 0.20
            quantidade -= 20

            # Calcula o custo das fotocópias restantes
            fatura += quantidade * 0.10

# Exibe o valor da fatura
print(f"Valor total da fatura: R$ {fatura:.2f}")
