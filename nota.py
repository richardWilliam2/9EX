# Solicita ao usuário para inserir uma nota
nota = float(input("Digite uma nota (entre 0 e 20): "))

# Verifica se a nota está dentro do intervalo permitido
if 0 <= nota <= 20:
    if nota > 10:
        print("Nota validada")
    else:
        print("Nota não validada")
else:
    print("Nota inválida. Por favor, insira um valor entre 0 e 20.")
