def imprimir_intervalo(a, b):
    # Verifica se 'a' é menor que 'b'
    # Neste caso, os valores devem ser impressos em ordem decrescente de 'b' até 'a'
    if a < b:
        for i in range(b, a - 1, -1):  # Inicia em 'b' e vai até 'a' (inclusive), decrementando
            print(i, end=" ")  # Imprime os valores no mesmo formato, separados por espaço
    # Verifica se 'a' é maior que 'b'
    # Se 'a' for maior que 'b', os valores estão fora de ordem e imprime "Valores inválidos"
    elif a > b:
        print("Valores inválidos")
    # Se 'a' for igual a 'b', imprime o valor de 'a' (ou 'b', já que são iguais)
    else:
        print(a)  # Se 'a' e 'b' forem iguais, imprime o valor único

# Solicita ao usuário para digitar o valor inicial 'a'
a = int(input("Digite o valor inicial (a): "))

# Solicita ao usuário para digitar o valor final 'b'
b = int(input("Digite o valor final (b): "))

# Chama a função 'imprimir_intervalo' para exibir os números do intervalo conforme as condições
imprimir_intervalo(a, b)
