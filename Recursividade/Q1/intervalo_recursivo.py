def imprimir_intervalo(a, b):
    # Verifica se 'a' é maior que 'b'
    # Se for, os valores estão fora de ordem, então imprime uma mensagem de erro
    if a > b:
        print("Valores inválidos")
    else:
        # Caso base: se 'a' for igual a 'b', imprime o valor e termina
        if a == b:
            print(a)
        else:
            # Se 'a' for menor que 'b', imprime 'a' e chama a função novamente com 'a + 1'
            # Isso faz com que o programa continue imprimindo os números até 'b'
            print(a, end=" ")
            imprimir_intervalo(a + 1, b)  # Chama a função de novo com 'a + 1'

# Aqui pedimos ao usuário para digitar o valor inicial 'a'
a = int(input("Digite o valor inicial (a): "))

# Agora pedimos ao usuário para digitar o valor final 'b'
b = int(input("Digite o valor final (b): "))

# Chama a função 'imprimir_intervalo' para mostrar os números entre 'a' e 'b'
imprimir_intervalo(a, b)
